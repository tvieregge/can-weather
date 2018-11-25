import csv

with open("output") as data_file:
    data = csv.reader(data_file)
    months = list(range(1,13))
    print(months)

    def filter_data(month):
        print(month)
        return list(filter(lambda datum: int(datum[1])==month, data))

    print(filter_data(3))
    # print(
    #     list(
    #         map(filter_data, months)))
