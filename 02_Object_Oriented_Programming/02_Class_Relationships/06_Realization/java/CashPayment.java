/**
 * Realization — CashPayment implements Payment.
 */
public class CashPayment implements Payment {

    @Override
    public void pay(double amount) {
        System.out.println("Paid $" + amount + " using Cash.");
    }

    @Override
    public String getPaymentMethod() {
        return "Cash";
    }
}
