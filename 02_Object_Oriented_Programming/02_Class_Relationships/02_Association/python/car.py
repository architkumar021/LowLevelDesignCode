"""
Association — Car class in Python.
"""


class Car:
    """Represents a car that can be driven."""

    def __init__(self, model: str) -> None:
        self._model = model

    @property
    def model(self) -> str:
        return self._model

    def drive(self) -> None:
        print(f"Driving a {self._model}")

    def __str__(self) -> str:
        return f"Car({self._model})"
