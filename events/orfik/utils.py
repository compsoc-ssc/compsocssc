import io
import base64
import random
import matplotlib.pyplot as plt
import pandas as pd

def jitter(iterable):
    return [i + ((1 if random.random() > 0.5 else -1) *
        random.random() * 0.05) for i in iterable]

def get_plot_string(attempts, orfik, max_question):
    "Given attempts, orfik, and max_question limit return a graph string"
    df = pd.DataFrame([(i.stamp, i.player) for i in attempts], columns=['stamp', 'player'])
    counts = df.groupby('player').count()
    temp = list(zip(counts.stamp, [str(i) for i in counts.index]))
    temp.sort(reverse=True)
    name_to_rank = {i[1]: 1 + index for index, i in enumerate(temp)}
    with plt.style.context('ggplot'):
        plt.figure(figsize=(15, 5))
        plt.gca().set_xlim([orfik.start_time, orfik.end_time])
        plt.gca().set_ylim([0,  max_question])
        plt.xlabel('Contest Timeline')
        plt.ylabel('Question Levels')
        for name, group in df.groupby('player'):
            label = '{:2}. {}'.format(name_to_rank[str(name)], name)
            plt.plot(group.stamp, jitter(range(group.shape[0])), '.-', label=label)
        handles,labels = plt.gca().get_legend_handles_labels()
        temp = list(sorted(zip(labels, handles), key=lambda x: x[0]))
        labels, handles = [i[0] for i in temp], [i[1] for i in temp]
        plt.gca().legend(handles, labels, bbox_to_anchor=(1.1, 1.0))
        plt.title(orfik.name)
        # Save to string
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.getvalue())
        plt.close()
    return string
