import csv
from collections import defaultdict
import matplotlib.pyplot as plt

def filter_data(data, month):
    return [(int(entry[0]), float(entry[3]))
            for entry in filter(lambda datum: int(datum[1])==month, data)]

def group_days(l):
    by_year = defaultdict(list)
    for entry in l:
        by_year[entry[0]].append(entry[1])
    return by_year

def avg_dict(data):
    return [(year, sum(data[year])/len(data[year]))
            for year in data.keys()]

def do_month(data, month):
    return tuple(
            avg_dict(
            group_days(
            filter_data(data, month))))

def window(l, index, aperture):
    if index >= len(l)-half_ap or index < half_ap:
        return []
    left = index-half_ap
    right = index+half_ap
    temp = [l[left:right]]
    temp.extend(window(l, index+1, half_ap))
    return temp

def avg(l):
    return sum(l)/(len(l) or 1)

def running_avg(l, aperture):
    return list(map(avg, (window(l, half_ap, half_ap))))

with open("output") as data_file:
    months = tuple(range(1,13))
    data = tuple(csv.reader(data_file))
    results = [do_month(data, month) for month in months]

    aperture = 5
    half_ap = aperture//2
    month1 = sorted(results[1])
    x_val = [datum[0] for datum in month1]
    y_val = [datum[1] for datum in month1]
    plt.plot(x_val[half_ap:-half_ap], running_avg(y_val, half_ap))
    plt.show()

