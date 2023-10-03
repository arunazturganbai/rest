# Singleton Design Pattern
class RestaurantManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RestaurantManager, cls).__new__(cls)
            cls._instance.menu = {}
            cls._instance.orders = []
        return cls._instance

    def add_item_to_menu(self, item_name, price):
        self.menu[item_name] = price

    def place_order(self, table_number, order_items, payment_strategy):
        total_cost = sum(self.menu[item] for item in order_items)
        self.orders.append({"table_number": table_number, "items": order_items, "total_cost": total_cost})
        payment_strategy.pay(total_cost)

