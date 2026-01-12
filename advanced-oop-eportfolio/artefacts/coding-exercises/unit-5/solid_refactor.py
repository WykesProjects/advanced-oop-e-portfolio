from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

class PaymentStrategy(ABC):
    # Strategy interface that defines a common payment operation

    @abstractmethod
    def pay(self, amount: float) -> None:
        # Execute payment strategy for a given amount
        raise NotImplementedError

@dataclass(frozen=True)
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Processing credit card payment of ${amount:.2f}")

@dataclass(frozen=True)
class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Processing PayPal payment of ${amount:.2f}")

@dataclass(frozen=True)
class BankTransferPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Processing bank transfer of ${amount:.2f}")

class PaymentProcessor:
    # Context class that delegates payment processing to a strategy

    def __init__(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        # Allow the strategy to be changed at runtime
        self._strategy = strategy

    def process_payment(self, amount: float) -> None:
        # Delegate payment logic to the configured strategy
        self._strategy.pay(amount)

def demo() -> None:
    processor = PaymentProcessor(CreditCardPayment())
    processor.process_payment(25)

    processor.set_strategy(PayPalPayment())
    processor.process_payment(40)

    processor.set_strategy(BankTransferPayment())
    processor.process_payment(120)

if __name__ == "__main__":
    demo()
