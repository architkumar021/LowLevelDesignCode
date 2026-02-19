"""
Driver — demonstrates Aggregation (HAS-A with weak ownership).
Run: python main.py
"""

from player import Player
from team import Team


def main() -> None:
    p1 = Player("Stephen", 30)
    p2 = Player("Klay", 11)
    p3 = Player("Draymond", 23)

    team = Team("Warriors")
    team.add_player(p1)
    team.add_player(p2)
    team.add_player(p3)
    team.show_team()

    # Remove a player — the player object still exists
    team.remove_player(p2)
    print("\nAfter removing Klay:")
    team.show_team()
    print(f"\nKlay still exists: {p2}")


if __name__ == "__main__":
    main()

"""
Expected Output:
Team Warriors has players:
  - Stephen (#30)
  - Klay (#11)
  - Draymond (#23)

After removing Klay:
Team Warriors has players:
  - Stephen (#30)
  - Draymond (#23)

Klay still exists: Klay (#11)
"""
