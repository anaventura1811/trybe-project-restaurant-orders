class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_dishes_per_customer(self, customer):
        list_of_orders = self.orders
        dishes_by_client = {}
        for client, order, day in list_of_orders:
            if client == customer:
                if order not in dishes_by_client:
                    dishes_by_client[order] = 1
                else:
                    dishes_by_client[order] += 1
        return dishes_by_client

    def get_menu(self):
        list_of_orders = self.orders
        menu = []
        for _a, order, _c in list_of_orders:
            if order not in menu:
                menu.append(order)
        return menu

    def get_most_ordered_dish_per_costumer(self, costumer):
        list_of_orders = self.get_dishes_per_customer(costumer)
        dishes = list_of_orders.items()
        most_ordered = 0
        dish_name = ''
        for order, frequency in dishes:
            if frequency > most_ordered:
                most_ordered = frequency
                dish_name = order
        return dish_name

    def get_never_ordered_per_costumer(self, costumer):
        menu = self.get_menu(self)
        list_of_orders = self.get_dishes_per_customer(self, costumer)
        dishes_never_ordered = menu.difference(list_of_orders)
        return dishes_never_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        list_of_orders = self.orders
        list_of_days = []
        list_of_days_at_restaurant = []
        for client, order, day in list_of_orders:
            if day not in list_of_days:
                list_of_days.append(day)
            if client == costumer:
                if day not in list_of_days_at_restaurant:
                    list_of_days_at_restaurant.append(day)
        set_list_week_days = set(list_of_days)
        set_days_at_restaurant = set(list_of_days_at_restaurant)
        return set_list_week_days.difference(set_days_at_restaurant)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
