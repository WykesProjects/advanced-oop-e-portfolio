from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

class DiscountStrategy(ABC):
    # Strategy interface for applying a discount to a price

    @abstractmethod
    def apply(self, price: float) -> float:
        raise NotImplementedError

@dataclass(frozen=True)
class NoDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price

@dataclass(frozen=True)
class BookDiscount(DiscountStrategy):
    factor: float = 0.90

    def apply(self, price: float) -> float:
        return price * self.factor

@dataclass(frozen=True)
class ElectronicsDiscount(DiscountStrategy):
    factor: float = 0.80

    def apply(self, price: float) -> float:
        return price * self.factor

class DiscountRegistry:
    # Resolves an item type to its discount strategy

    def __init__(self) -> None:
        self._strategies: dict[str, DiscountStrategy] = {
            "book": BookDiscount(),
            "electronics": ElectronicsDiscount(),
        }
        self._default: DiscountStrategy = NoDiscount()

    def get_strategy(self, item_type: str | None) -> DiscountStrategy:
        if item_type is None:
            return self._default
        return self._strategies.get(item_type, self._default)

def calculate_total_price(items: list[dict], registry: DiscountRegistry | None = None) -> float:
    if registry is None:
        registry = DiscountRegistry()

    total = 0.0

    for item in items:
        item_type = item.get("type")
        price = float(item.get("price", 0.0))

        strategy = registry.get_strategy(item_type)
        total += strategy.apply(price)

    return total

def demo() -> None:
    items = [
        {"type": "book", "price": 10},
        {"type": "electronics", "price": 100},
        {"type": "other", "price": 5},
    ]
    print(calculate_total_price(items))

if __name__ == "__main__":
    demo()
