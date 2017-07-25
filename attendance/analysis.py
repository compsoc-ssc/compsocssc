import pandas as pd
from pickle import load


def make_table(data):
    table = []
    for key, json in data.items():
        course, sem, month = key
        for person in json['data']:
            pid = person['id']
            d = person['values']
            name = d['name']
            tla = d['Tla']
            tld = d['Tld']
            tpa = d['Tpa']
            tpd = d['Tpd']
            tta = d['Tta']
            ttd = d['Ttd']
            row = (pid, name, course, sem, month, tla, tld, tpa, tpd, tta, ttd)
            table.append(row)

    df = pd.DataFrame(table, columns=['pid', 'name', 'course', 'sem',
                                      'month', 'tla', 'tld', 'tpa', 'tpd',
                                      'tta', 'ttd'])

    df['percent_la'] = 100 * (df.tla / df.tld)
    df['percent_pa'] = 100 * (df.tpa / df.tpd)
    df['percent_ta'] = 100 * (df.tta / df.ttd)
    df['course'] = df['pid'].str[3:6]
    df['month'] = df.month.map({1: 'Jan', 8: 'July&Aug', 9: 'Sep', 10: 'Oct'})
    df['admission_year'] = ('20' + df['pid'].str[:2]).astype(int)
    return df


if __name__ == '__main__':
    with open('attendance.pickle', 'rb') as fl:
        data = load(fl)
    print(make_table(data))
