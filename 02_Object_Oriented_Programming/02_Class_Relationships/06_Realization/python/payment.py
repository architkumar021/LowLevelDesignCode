"""
Realization — Payment interface (abstract base class) in Python.

Python uses ABC (Abstract Base Class) to enforce interface contracts.
"""

from abc import ABC, abstractmethod


class Payment(ABC):
    """Interface: every payment type must implement pay() and payment_method."""

    @abstractmethod
    def pay(self, amount: float) -> None:
        ...

    @property
    @abstractmethod
    def payment_method(self) -> str:
        ...
