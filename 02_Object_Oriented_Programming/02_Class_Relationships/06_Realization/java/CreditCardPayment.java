/**
 * Realization — CreditCardPayment implements Payment.
 */
public class CreditCardPayment implements Payment {

    private String cardNumber;

    public CreditCardPayment(String cardNumber) {
        this.cardNumber = cardNumber;
    }

    @Override
    public void pay(double amount) {
        String masked = "****-" + cardNumber.substring(cardNumber.length() - 4);
        System.out.println("Paid $" + amount + " using Credit Card (" + masked + ").");
    }

    @Override
    public String getPaymentMethod() {
        return "Credit Card";
    }
}
