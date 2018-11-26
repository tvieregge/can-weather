import csv
import os

directory = "./data"

with open("output", 'w') as output_file:
    removed_count = 0
    total_count = 0
    output_writer = csv.writer(output_file)
    for filename in os.listdir(directory):
        if not filename.endswith(".csv"):
            continue

        with open("./data/" + filename) as data_file:
            reader = csv.reader(data_file)
            for row in reader:
                if row and row[0] == 'Date/Time':
                    break

            for row in reader:
                data = [row[i] for i in [1,2,3,5,7]]
                if data[0] == 'Year':
                    print(row)
                    print(filename)
                if data.count('') == 0:
                    output_writer.writerow(data)
                else:
                    removed_count += 1
                total_count += 1

    print("removed {}/{} entries because of missing data".format(removed_count, total_count))

