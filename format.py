import csv
import os

data_start = 25
directory = "./data"

with open("output", 'w') as output_file:
    removed_count = 0
    total_count = 0
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
                if data.count('') == 0:
                    output_writer.writerow(data)
                else:
                    removed_count += 1
                total_count += 1

    print("removed {}/{} entries because of missing data".format(removed_count, total_count))

