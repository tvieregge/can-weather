import csv
from collections import defaultdict

def filter_data(data, month):
    return [(int(entry[0]), float(entry[3]))
            for entry in filter(lambda datum: int(datum[1])==month, data)]

def group(l):
    by_year = defaultdict(list)
    for entry in l:
        by_year[entry[0]].append(entry[1])
    return by_year

def avg(data):
    return [(year, sum(data[year])/len(data[year]))
            for year in data.keys()]

with open("output") as data_file:
    data = list(csv.reader(data_file))
    print(
    list(
    avg(
    group(filter_data(data, 1)))))

