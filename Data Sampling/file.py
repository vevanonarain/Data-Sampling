import csv
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
population_std_deviation = statistics.stdev(data)

print("Population mean --> ", population_mean)
print("Population Std Deviation --> ", population_std_deviation)

def random_set_of_means(counter):
    dataset = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]

        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    sampling_mean = statistics.mean(mean_list)
    print("Sampling Mean --> ", sampling_mean)

    fig = ff.create_distplot([mean_list], ["Reading Time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[sampling_mean, sampling_mean], y=[0, 1], mode="lines", name="Mean"))
    fig.show()

def setup():
    mean_list = []

    for i in range(0, 100):
        set_of_means = random_set_of_means(30)
        mean_list.append(set_of_means)

    show_fig(mean_list)

setup()