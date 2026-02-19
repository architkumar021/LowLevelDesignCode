"""
main.py - Driver script to demonstrate Classes and Objects in Python

Shows:
    - Creating objects (instances) from a class
    - Invoking methods on objects
    - Accessing state through properties
    - Object behaviour influenced by internal state

Run:  python main.py
"""

from car import Car


def main() -> None:
    # ── Creating objects ─────────────────────────────────────────────────
    car1 = Car("Toyota", "Corolla", 2021)
    car2 = Car("Honda", "Civic", 2022)

    # ── Display initial info ─────────────────────────────────────────────
    car1.display_info()
    car2.display_info()
    print()

    # ── Start engines ────────────────────────────────────────────────────
    car1.start_engine()
    car2.start_engine()
    car1.start_engine()  # trying to start again — already running
    print()

    # ── Accelerate & brake ───────────────────────────────────────────────
    car1.accelerate(60)
    car1.accelerate(40)
    car1.brake(30)
    print()

    # ── Try to stop engine while moving ──────────────────────────────────
    car1.stop_engine()   # should warn — still moving
    car1.brake(70)       # bring to 0
    car1.stop_engine()   # now it works
    print()

    # ── Final state ──────────────────────────────────────────────────────
    car1.display_info()
    car2.display_info()

    # ── Bonus: repr output ───────────────────────────────────────────────
    print(f"\nrepr(car1) = {repr(car1)}")
    print(f"repr(car2) = {repr(car2)}")


if __name__ == "__main__":
    main()


"""
Expected Output:
────────────────
Car Info: Toyota Corolla (2021) | Engine: OFF | Speed: 0 km/h
Car Info: Honda Civic (2022) | Engine: OFF | Speed: 0 km/h

2021 Toyota Corolla → Engine started.
2022 Honda Civic → Engine started.
2021 Toyota Corolla → Engine is already running.

2021 Toyota Corolla → Accelerated to 60 km/h.
2021 Toyota Corolla → Accelerated to 100 km/h.
2021 Toyota Corolla → Braked to 70 km/h.

2021 Toyota Corolla → Cannot stop engine while moving! Current speed: 70 km/h
2021 Toyota Corolla → Braked to 0 km/h.
2021 Toyota Corolla → Engine stopped.

Car Info: Toyota Corolla (2021) | Engine: OFF | Speed: 0 km/h
Car Info: Honda Civic (2022) | Engine: ON | Speed: 0 km/h

repr(car1) = Car(manufacturer='Toyota', model='Corolla', year=2021)
repr(car2) = Car(manufacturer='Honda', model='Civic', year=2022)
"""
