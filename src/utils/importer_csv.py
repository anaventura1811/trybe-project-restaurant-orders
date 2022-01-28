import csv


def read_and_parse_csv_file(path: str) -> list:
    with open(path, mode="r") as csv_file:
        reader = csv.reader(csv_file)
        return [row for row in reader]

# print(read_and_parse_csv_file('data/orders_1.csv'))
#  a, b e c