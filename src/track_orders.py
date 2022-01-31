class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

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
        menu = set(self.get_menu())
        list_of_orders = self.get_dishes_per_customer(costumer)
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

    def get_customer_orders_per_day(self):
        customer_orders_per_day = {}
        list_of_orders = self.orders
        for _customer, _order, day in list_of_orders:
            if day not in customer_orders_per_day:
                customer_orders_per_day[day] = 1
            else:
                customer_orders_per_day[day] += 1
        return customer_orders_per_day

    def get_busiest_day_qtd(self):
        customer_orders_per_day = self.get_customer_orders_per_day()
        most_orders = 0
        for day, qtd in customer_orders_per_day.items():
            if qtd > most_orders:
                most_orders = qtd
        return most_orders

    def get_order_frequency_per_costumer(self, costumer, order):
        dishes_per_customer = self.get_dishes_per_customer(costumer)
        frequency = 0
        for dish, qtd in dishes_per_customer:
            if dish == order:
                frequency = qtd
        return frequency

    def get_busiest_day(self):
        customer_orders_per_day = self.get_customer_orders_per_day()
        most_orders = 0
        busiest_day = ''
        for day_of_week, qtd in customer_orders_per_day.items():
            if qtd > most_orders:
                most_orders = qtd
                busiest_day = day_of_week
        return busiest_day

    def get_least_busy_day(self):
        customer_orders_per_day = self.get_customer_orders_per_day()
        most_orders = self.get_busiest_day_qtd()
        least_busy_day = ''
        for day, qtd in customer_orders_per_day.items():
            if qtd < most_orders:
                most_orders = qtd
                least_busy_day = day
        return least_busy_day
