# Strategy Design Pattern
class PaymentStrategy:
    def pay(self, total_cost):
        pass


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, expiry_date):
        self.card_number = card_number
        self.expiry_date = expiry_date

    def pay(self, total_cost):
        print(f"Paid ${total_cost:.2f} with Credit Card ({self.card_number})")


class CashPayment(PaymentStrategy):
    def pay(self, total_cost):
        print(f"Paid ${total_cost:.2f} in cash")
