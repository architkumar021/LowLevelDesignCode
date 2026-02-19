"""
Aggregation — Player class in Python.
"""


class Player:
    """Represents a player who can exist independently of any team."""

    def __init__(self, name: str, jersey_number: int) -> None:
        self._name = name
        self._jersey_number = jersey_number

    @property
    def name(self) -> str:
        return self._name

    @property
    def jersey_number(self) -> int:
        return self._jersey_number

    def __str__(self) -> str:
        return f"{self._name} (#{self._jersey_number})"

    def __repr__(self) -> str:
        return f"Player('{self._name}', {self._jersey_number})"
