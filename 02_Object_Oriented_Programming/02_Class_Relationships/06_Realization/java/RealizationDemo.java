/**
 * Driver — demonstrates Realization (interface implementation).
 *
 * All payment types share the same contract (Payment interface).
 * We can process them polymorphically.
 */
public class RealizationDemo {

    public static void processPayment(Payment payment, double amount) {
        System.out.print("[" + payment.getPaymentMethod() + "] ");
        payment.pay(amount);
    }

    public static void main(String[] args) {
        Payment creditCard = new CreditCardPayment("4111111111111234");
        Payment cash = new CashPayment();
        Payment upi = new UpiPayment("alice@upi");

        processPayment(creditCard, 99.99);
        processPayment(cash, 25.00);
        processPayment(upi, 150.50);
    }
}

/*
Expected Output:
[Credit Card] Paid $99.99 using Credit Card (****-1234).
[Cash] Paid $25.0 using Cash.
[UPI] Paid $150.5 via UPI (alice@upi).
*/
