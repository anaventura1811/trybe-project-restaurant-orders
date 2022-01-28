import csv


def read_and_parse_csv_file(path: str) -> list:
    with open(path, mode="r") as csv_file:
        reader = csv.reader(csv_file)
        return [row for row in reader]

# read_and_parse_csv_file('data/orders_1.csv')
list_of_orders = read_and_parse_csv_file('data/orders_1.csv')
clients = []
for a, b, c in list_of_orders:
    # print (a)
    clients.append(a)
# print(set(clients))
    
#  a, b e c