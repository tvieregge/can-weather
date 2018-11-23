import csv
import os

data_start = 25
directory = "./data"

with open("output", 'w') as output_file:
    output_writer = csv.writer(output_file)
    for filename in os.listdir(directory):
        if not filename.endswith(".csv"):
            continue

        with open("./data/" + filename) as data_file:
            for i in range(data_start):
                next(data_file)

            reader = csv.reader(data_file)
            for row in reader:
                #print(row)
                data = [row[i] for i in [1,2,3,5,7]]
                output_writer.writerow(data)
