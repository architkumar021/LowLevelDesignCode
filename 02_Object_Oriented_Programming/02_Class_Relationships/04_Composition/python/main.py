"""
Driver — demonstrates Composition (strong HAS-A, owned lifecycle).
Run: python main.py
"""

from house import House


def main() -> None:
    house = House("123 Main Street")
    house.show_house()


if __name__ == "__main__":
    main()

"""
Expected Output:
House at 123 Main Street contains:
  - Living Room (350 sq ft)
  - Kitchen (200 sq ft)
  - Bedroom (300 sq ft)
  - Bathroom (100 sq ft)
  Total area: 950 sq ft
"""
