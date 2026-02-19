"""
Association — Person class in Python.

A Person is associated with a Car.
The Car is passed in from outside — Person does NOT create it.
Both can exist independently.
"""

from car import Car


class Person:
    """A person who is associated with a car."""

    def __init__(self, name: str, car: Car) -> None:
        self._name = name
        self._car = car  # Association: Person "has a" Car

    @property
    def name(self) -> str:
        return self._name

    @property
    def car(self) -> Car:
        return self._car

    @car.setter
    def car(self, car: Car) -> None:
        self._car = car

    def go_for_drive(self) -> None:
        print(f"{self._name} is going for a drive.")
        self._car.drive()

    def __str__(self) -> str:
        return f"Person({self._name}, car={self._car})"
