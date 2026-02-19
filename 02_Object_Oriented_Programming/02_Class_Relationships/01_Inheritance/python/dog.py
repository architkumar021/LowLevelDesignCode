"""
Inheritance — derived class (subclass) in Python.

Dog extends Animal → inherits eat() and sleep(),
and adds its own behaviour: bark().
"""

from animal import Animal


class Dog(Animal):
    """A dog is a specialised animal with a breed and bark."""

    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name)  # call parent constructor
        self._breed = breed

    @property
    def breed(self) -> str:
        return self._breed

    def bark(self) -> None:
        print(f"{self.name} barks: Woof Woof!")

    def __str__(self) -> str:
        return f"Dog({self.name}, breed={self._breed})"

    def __repr__(self) -> str:
        return f"Dog(name='{self.name}', breed='{self._breed}')"
