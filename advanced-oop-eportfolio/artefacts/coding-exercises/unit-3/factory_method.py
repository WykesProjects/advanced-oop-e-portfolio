from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Final

class Car(ABC):
    # Abstract product that defines the common interface for all cars

    @abstractmethod
    def drive(self) -> str:
        # Method that defines how a car is driven
        raise NotImplementedError

@dataclass(frozen=True)
class Sedan(Car):
    model: Final[str] = "Sedan"

    def drive(self) -> str:
        return f"{self.model}: Smooth cruising, optimised for comfort and efficiency."

@dataclass(frozen=True)
class SUV(Car):
    model: Final[str] = "SUV"

    def drive(self) -> str:
        return f"{self.model}: Confident handling, suitable for rougher terrain and family trips."

@dataclass(frozen=True)
class Hatchback(Car):
    model: Final[str] = "Hatchback"

    def drive(self) -> str:
        return f"{self.model}: Compact and agile, ideal for city driving and tight parking."

class CarFactory(ABC):
    # Abstract creator class responsible for defining the factory method

    @abstractmethod
    def create_car(self) -> Car:
        # Factory method that returns a Car
        raise NotImplementedError

    def build_and_test_drive(self) -> str:
        # Common workflow that delegates object creation to subclasses
        car = self.create_car()
        return car.drive()

class SedanFactory(CarFactory):
    def create_car(self) -> Car:
        return Sedan()

class SUVFactory(CarFactory):
    def create_car(self) -> Car:
        return SUV()

class HatchbackFactory(CarFactory):
    def create_car(self) -> Car:
        return Hatchback()

def demo() -> None:
    registry: dict[str, CarFactory] = {
        "sedan": SedanFactory(),
        "suv": SUVFactory(),
        "hatchback": HatchbackFactory(),
    }

    requested = ["sedan", "suv", "hatchback"]

    for car_type in requested:
        factory = registry[car_type]
        print(factory.build_and_test_drive())

if __name__ == "__main__":
    demo()
