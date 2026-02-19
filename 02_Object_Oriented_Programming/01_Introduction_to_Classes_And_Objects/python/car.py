"""
car.py - Demonstrates Classes and Objects in Python

Key Concepts:
    - Class definition with __init__ (constructor)
    - Encapsulation via name-mangling (_ convention & @property)
    - Instance methods that operate on internal state
    - __str__ and __repr__ dunder methods
    - Type hints for better readability
"""


class Car:
    """Represents a car with basic driving behaviour."""

    # ── Constructor ──────────────────────────────────────────────────────
    def __init__(self, manufacturer: str, model: str, year: int) -> None:
        self._manufacturer = manufacturer
        self._model = model
        self._year = year
        self._engine_running: bool = False
        self._speed: int = 0  # km/h

    # ── Properties (getters / setters) ───────────────────────────────────
    @property
    def manufacturer(self) -> str:
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str) -> None:
        self._manufacturer = value

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        self._model = value

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        self._year = value

    @property
    def engine_running(self) -> bool:
        return self._engine_running

    @property
    def speed(self) -> int:
        return self._speed

    # ── Behaviours / Methods ─────────────────────────────────────────────
    def start_engine(self) -> None:
        """Start the car's engine."""
        if self._engine_running:
            print(f"{self} → Engine is already running.")
            return
        self._engine_running = True
        print(f"{self} → Engine started.")

    def stop_engine(self) -> None:
        """Stop the car's engine (only when stationary)."""
        if not self._engine_running:
            print(f"{self} → Engine is already off.")
            return
        if self._speed > 0:
            print(
                f"{self} → Cannot stop engine while moving! "
                f"Current speed: {self._speed} km/h"
            )
            return
        self._engine_running = False
        print(f"{self} → Engine stopped.")

    def accelerate(self, increment: int) -> None:
        """Increase speed by *increment* km/h."""
        if not self._engine_running:
            print(f"{self} → Start the engine first!")
            return
        self._speed += increment
        print(f"{self} → Accelerated to {self._speed} km/h.")

    def brake(self, decrement: int) -> None:
        """Decrease speed by *decrement* km/h (min 0)."""
        if self._speed == 0:
            print(f"{self} → Car is already stationary.")
            return
        self._speed = max(0, self._speed - decrement)
        print(f"{self} → Braked to {self._speed} km/h.")

    def display_info(self) -> None:
        """Print a summary of the car's current state."""
        engine_status = "ON" if self._engine_running else "OFF"
        print(
            f"Car Info: {self._manufacturer} {self._model} ({self._year})"
            f" | Engine: {engine_status}"
            f" | Speed: {self._speed} km/h"
        )

    # ── Dunder methods ───────────────────────────────────────────────────
    def __str__(self) -> str:
        return f"{self._year} {self._manufacturer} {self._model}"

    def __repr__(self) -> str:
        return (
            f"Car(manufacturer='{self._manufacturer}', "
            f"model='{self._model}', year={self._year})"
        )
