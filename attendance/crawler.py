import time
import random
import requests
from itertools import product
from threading import Thread
from multiprocessing import Queue
from queue import Empty


# Global definitions
dataQueue = Queue()
base = 'http://sscattendance.formistry.com/'
base += 'report/data/attendance_{}_s{}_{}.json?96894'


# Function which crawls
def save_link_data(course, semester, month, base, queue):
    "Save this link's data to the queue"
    # Make the link to get
    url = base.format(course, semester, month)
    json, code = None, None
    for _ in range(5):
        try:
            # Timeout so we don't hang indefinitely
            page = requests.get(url, timeout=2)
            code = page.status_code
        except:
            time.sleep(random.random()*5)  # We don't want livelock
        else:
            break
    if code == 200:
        json = page.json()
    ins = [course, semester, month, json]
    queue.put(ins)


def get_attendance(base=None):
    """Base url with proper formatting

       http://sscattendance.formistry.com/report/data/attendance_{}_s{}_{}.json?96894
    """
    if base is None:
        base = 'http://sscattendance.formistry.com/'
        base += 'report/data/attendance_{}_s{}_{}.json?9689'
    # Generate arguments and threads
    args = list(product(range(1, 34), [1, 2, 3, 4], [8, 9, 10, 1, 2]))
    args = [(i, j, k, base, dataQueue) for i, j, k in args]
    threads = [Thread(target=save_link_data, args=arg)
               for arg in args]

    # Start threads
    [t.start() for t in threads]

    # Wait for them to finish
    while threads:
        new_threads = [t for t in threads if t.is_alive()]
        threads = new_threads
        print('{} left'.format(len(threads)), end='\r')

    # --------retreive data from queue
    data = {}
    while True:
        try:
            course, semester, month, json = dataQueue.get(block=False)
        except Empty:
            break
        else:
            data[course, semester, month] = json
    return data


if __name__ == '__main__':
    from pickle import dump
    data = get_attendance()
    with open('attendance.pickle', 'wb') as fl:
        dump(data, fl)
