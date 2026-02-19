"""
Realization — UpiPayment implements Payment.
"""

from payment import Payment


class UpiPayment(Payment):
    """Pays using UPI."""

    def __init__(self, upi_id: str) -> None:
        self._upi_id = upi_id

    @property
    def payment_method(self) -> str:
        return "UPI"

    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} via UPI ({self._upi_id}).")
