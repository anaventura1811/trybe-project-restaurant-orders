import csv


def read_and_parse_csv_file(path: str) -> list:
    with open(path, mode="r") as csv_file:
        reader = csv.reader(csv_file)
        return [row for row in reader]


def get_list_of_orders_by_client(client_name: str, path: str):
    list_of_orders = read_and_parse_csv_file(path)
    orders_count_by_product = {}
    for client, order, day_of_week in list_of_orders:
        if client == client_name:
            if order not in orders_count_by_product:
                orders_count_by_product[order] = 1
            else:
                orders_count_by_product[order] += 1
    return orders_count_by_product


def get_menu(path: str):
    list_of_orders = read_and_parse_csv_file(path)
    menu = []
    for _a, order, _c in list_of_orders:
        if order not in menu:
            menu.append(order)
    return menu


def get_most_ordered_dish_by_client(client_name: str, path: str):
    list_of_orders = get_list_of_orders_by_client(
        client_name, path)
    dishes = list_of_orders.items()
    most_ordered = 0
    dish_name = ''
    for order, frequency in dishes:
        if frequency > most_ordered:
            most_ordered = frequency
            dish_name = order
    return dish_name


def how_often_dish_was_ordered(
    client_name: str,
    dish_name: str,
    path: str
):
    list_of_orders = get_list_of_orders_by_client(client_name, path)
    dishes = list_of_orders.items()
    how_often = 0
    for order, frequency in dishes:
        if dish_name == order:
            how_often = frequency
    return how_often


def list_never_ordered_dishes(client_name: str, path: str):
    menu = set(get_menu(path))
    list_of_orders = get_list_of_orders_by_client(client_name, path)
    difference = menu.difference(list_of_orders)
    # never_ordered_list = set()
    # for item in difference:
    #     if item not in never_ordered_list:
    #         never_ordered_list.add(item)
    return difference


def never_been_at_restaurant(client_name: str, path: str):
    list_of_orders = read_and_parse_csv_file(path)
    list_of_days = []
    list_of_days_at_restaurant = []
    for client, b, day_of_week in list_of_orders:
        if day_of_week not in list_of_days:
            list_of_days.append(day_of_week)
        if client == client_name:
            if day_of_week not in list_of_days_at_restaurant:
                list_of_days_at_restaurant.append(day_of_week)
    set_list_of_days = set(list_of_days)
    set_days_at_restaurant = set(list_of_days_at_restaurant)
    return set_list_of_days.difference(set_days_at_restaurant)
