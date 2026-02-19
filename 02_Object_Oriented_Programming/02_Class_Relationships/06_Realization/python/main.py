"""
Driver — demonstrates Realization (interface implementation via ABC).
Run: python main.py
"""

from payment import Payment
from credit_card_payment import CreditCardPayment
from cash_payment import CashPayment
from upi_payment import UpiPayment


def process_payment(payment: Payment, amount: float) -> None:
    print(f"[{payment.payment_method}] ", end="")
    payment.pay(amount)


def main() -> None:
    credit_card = CreditCardPayment("4111111111111234")
    cash = CashPayment()
    upi = UpiPayment("alice@upi")

    process_payment(credit_card, 99.99)
    process_payment(cash, 25.00)
    process_payment(upi, 150.50)


if __name__ == "__main__":
    main()

"""
Expected Output:
[Credit Card] Paid $99.99 using Credit Card (****-1234).
[Cash] Paid $25.0 using Cash.
[UPI] Paid $150.5 via UPI (alice@upi).
"""
