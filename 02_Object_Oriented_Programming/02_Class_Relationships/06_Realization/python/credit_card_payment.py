"""
Realization — CreditCardPayment implements Payment.
"""

from payment import Payment


class CreditCardPayment(Payment):
    """Pays using a credit card."""

    def __init__(self, card_number: str) -> None:
        self._card_number = card_number

    @property
    def payment_method(self) -> str:
        return "Credit Card"

    def pay(self, amount: float) -> None:
        masked = f"****-{self._card_number[-4:]}"
        print(f"Paid ${amount} using Credit Card ({masked}).")
