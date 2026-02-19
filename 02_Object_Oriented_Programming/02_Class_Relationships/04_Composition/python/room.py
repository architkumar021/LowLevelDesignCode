"""
Composition — Room class in Python.
"""


class Room:
    """A room that only exists as part of a House."""

    def __init__(self, name: str, area_sq_ft: float) -> None:
        self._name = name
        self._area_sq_ft = area_sq_ft

    @property
    def name(self) -> str:
        return self._name

    @property
    def area_sq_ft(self) -> float:
        return self._area_sq_ft

    def __str__(self) -> str:
        return f"{self._name} ({self._area_sq_ft} sq ft)"
