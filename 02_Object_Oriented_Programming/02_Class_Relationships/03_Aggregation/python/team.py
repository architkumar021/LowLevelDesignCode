"""
Aggregation — Team class in Python.

A Team aggregates Players — holds references but does NOT own lifecycle.
"""

from __future__ import annotations
from player import Player


class Team:
    """A team that aggregates externally-created players."""

    def __init__(self, team_name: str) -> None:
        self._team_name = team_name
        self._players: list[Player] = []

    @property
    def team_name(self) -> str:
        return self._team_name

    @property
    def players(self) -> list[Player]:
        return list(self._players)  # return copy

    def add_player(self, player: Player) -> None:
        self._players.append(player)

    def remove_player(self, player: Player) -> None:
        self._players.remove(player)

    def show_team(self) -> None:
        print(f"Team {self._team_name} has players:")
        for p in self._players:
            print(f"  - {p}")

    def __str__(self) -> str:
        return f"Team({self._team_name}, size={len(self._players)})"
