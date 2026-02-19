"""
Realization — CashPayment implements Payment.
"""

from payment import Payment


class CashPayment(Payment):
    """Pays using cash."""

    @property
    def payment_method(self) -> str:
        return "Cash"

    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} using Cash.")
