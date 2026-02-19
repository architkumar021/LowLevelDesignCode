"""
Driver — demonstrates Association (HAS-A, both independent).
Run: python main.py
"""

from car import Car
from person import Person


def main() -> None:
    car = Car("Tesla Model 3")
    person = Person("Alice", car)

    person.go_for_drive()

    # Re-associate with a different car
    new_car = Car("BMW i4")
    person.car = new_car
    print(f"\n{person.name} switched cars.")
    person.go_for_drive()


if __name__ == "__main__":
    main()

"""
Expected Output:
Alice is going for a drive.
Driving a Tesla Model 3

Alice switched cars.
Alice is going for a drive.
Driving a BMW i4
"""
