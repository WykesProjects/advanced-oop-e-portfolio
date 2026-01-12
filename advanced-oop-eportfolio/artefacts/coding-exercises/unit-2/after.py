from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    name: str
    price: float


class DiscountPolicy(ABC):
    # Small interface for discount behaviour (ISP)

    @abstractmethod
    def apply(self, subtotal: float) -> float:
        raise NotImplementedError


class NoDiscount(DiscountPolicy):
    def apply(self, subtotal: float) -> float:
        return subtotal


class PercentageDiscount(DiscountPolicy):
    def __init__(self, percent: float) -> None:
        if percent < 0 or percent > 100:
            raise ValueError("Discount percent must be between 0 and 100")
        self._percent = percent

    def apply(self, subtotal: float) -> float:
        return subtotal * (1 - (self._percent / 100))


class PaymentMethod(ABC):
    # Abstraction for payment methods (DIP)

    @abstractmethod
    def pay(self, amount: float) -> None:
        raise NotImplementedError


class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Processing credit card payment of £{amount:.2f}")


class PayPalPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Processing PayPal payment of £{amount:.2f}")


class BankTransferPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Processing bank transfer payment of £{amount:.2f}")


class PaymentProcessor:
    # Single responsibility: payment orchestration (SRP)

    def __init__(self, method: PaymentMethod) -> None:
        self._method = method

    def process(self, amount: float) -> None:
        self._method.pay(amount)


class Order:
    # Single responsibility: cart management and totals (SRP)

    def __init__(self, discount: DiscountPolicy | None = None) -> None:
        self._items: list[Product] = []
        self._discount = discount if discount is not None else NoDiscount()

    def add_item(self, item: Product) -> None:
        self._items.append(item)

    def subtotal(self) -> float:
        return sum(item.price for item in self._items)

    def total(self) -> float:
        return self._discount.apply(self.subtotal())


def demo() -> None:
    order = Order(discount=PercentageDiscount(10))
    order.add_item(Product("Keyboard", 49.99))
    order.add_item(Product("Mouse", 24.99))

    amount = order.total()

    processor = PaymentProcessor(PayPalPayment())
    processor.process(amount)


if __name__ == "__main__":
    demo()