import csv
from collections import defaultdict
import matplotlib.pyplot as plt

# Variables for controlling the analysis
#   data:column refers to the column in the "output" file
#   aperture refers to the width to use for the running average
data_column = 1
aperture = 1

def filter_data(data, month):
    return [(int(entry[0]), float(entry[3]))
            for entry in filter(lambda datum: int(datum[1])==month, data)]

def group_days(column, l):
    by_year = defaultdict(list)
    for entry in l:
        by_year[entry[0]].append(entry[column])
    return by_year

def process_month(data, month, data_column):
    return sorted(
            tuple(
            avg_years(
            group_days(data_column,
            filter_data(data, month)))))

def window(l, index, aperture):
    # don't want results that can't be averaged over the whole window
    if index >= len(l)-half_ap or index < half_ap:
        return []
    left = index-half_ap
    right = max(index+half_ap, index+1)
    temp = [l[left:right]]
    temp.extend(window(l, index+1, half_ap))
    return temp

def avg_years(data):
    return [(year, avg(data[year]))
            for year in data.keys()]

def avg(l):
    return sum(l)/(len(l) or 1)

def running_avg(l, aperture):
    return list(map(avg, (window(l, half_ap, half_ap))))

def clip_x_vals(x_vals, half_ap):
    if not half_ap:
        return x_vals
    return x_vals[half_ap:-half_ap]

with open("output") as data_file:
    months = tuple(range(1,13))
    data = tuple(csv.reader(data_file))
    results = [process_month(data, month, data_column) for month in months]

    half_ap = aperture//2
    for r in results:
        x_val = [datum[0] for datum in r]
        y_val = [datum[1] for datum in r]
        plt.plot(clip_x_vals(x_val, half_ap),
                 running_avg(y_val, half_ap))

    plt.legend(months, loc='best')
    plt.grid(True)
    plt.show()

