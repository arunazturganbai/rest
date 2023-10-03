# Client Code
if __name__ == "__main__":
    # Singleton pattern: Create a single instance of the RestaurantManager
    restaurant_manager = RestaurantManager()

    # Add items to the menu
    restaurant_manager.add_item_to_menu("Burger", 5.99)
    restaurant_manager.add_item_to_menu("Pizza", 8.99)
    restaurant_manager.add_item_to_menu("Salad", 3.49)

    # Place orders
    restaurant_manager.place_order(1, ["Burger", "Pizza"], CreditCardPayment("1234-5678-9012-3456", "12/25"))
    restaurant_manager.place_order(2, ["Salad"], CashPayment())

    # Get orders
    orders = restaurant_manager.orders
    for order in orders:
        print(f"Table {order['table_number']} ordered {', '.join(order['items'])}. Total cost: ${order['total_cost']:.2f}")