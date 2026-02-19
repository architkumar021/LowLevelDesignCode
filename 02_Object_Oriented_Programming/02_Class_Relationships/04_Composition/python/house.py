"""
Composition — House class in Python.

A House creates and owns its Rooms internally (strong ownership).
Rooms cannot exist without the House.
"""

from room import Room


class House:
    """A house composed of rooms it creates and owns."""

    def __init__(self, address: str) -> None:
        self._address = address
        # Rooms are created INSIDE the House — composition
        self._rooms: list[Room] = [
            Room("Living Room", 350),
            Room("Kitchen", 200),
            Room("Bedroom", 300),
            Room("Bathroom", 100),
        ]

    @property
    def address(self) -> str:
        return self._address

    @property
    def rooms(self) -> list[Room]:
        return list(self._rooms)  # return copy

    @property
    def total_area(self) -> float:
        return sum(r.area_sq_ft for r in self._rooms)

    def show_house(self) -> None:
        print(f"House at {self._address} contains:")
        for r in self._rooms:
            print(f"  - {r}")
        print(f"  Total area: {self.total_area} sq ft")

    def __str__(self) -> str:
        return f"House({self._address}, rooms={len(self._rooms)})"
