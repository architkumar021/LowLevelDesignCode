"""
Inheritance — base class (superclass) in Python.

Key concept: A Dog IS-A Animal.
The child class inherits fields & methods from the parent.
"""


class Animal:
    """Base class representing a generic animal."""

    def __init__(self, name: str = "Unknown") -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def eat(self) -> None:
        print(f"{self._name} is eating.")

    def sleep(self) -> None:
        print(f"{self._name} is sleeping.")

    def __str__(self) -> str:
        return f"Animal({self._name})"

    def __repr__(self) -> str:
        return f"Animal(name='{self._name}')"
