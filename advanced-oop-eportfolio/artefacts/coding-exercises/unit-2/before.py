class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item["price"] for item in self.items)

    def pay(self, payment_type):
        total = self.calculate_total()

        if payment_type == "credit":
            print(f"Processing credit card payment of £{total:.2f}")
        elif payment_type == "paypal":
            print(f"Processing PayPal payment of £{total:.2f}")
        elif payment_type == "bank_transfer":
            print(f"Processing bank transfer payment of £{total:.2f}")
        else:
            raise ValueError("Invalid payment type")


def demo():
    order = Order()
    order.add_item({"name": "Keyboard", "price": 49.99})
    order.add_item({"name": "Mouse", "price": 24.99})

    order.pay("paypal")


if __name__ == "__main__":
    demo()