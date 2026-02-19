/**
 * Realization — UpiPayment implements Payment.
 * Enhancement: added a third payment type.
 */
public class UpiPayment implements Payment {

    private String upiId;

    public UpiPayment(String upiId) {
        this.upiId = upiId;
    }

    @Override
    public void pay(double amount) {
        System.out.println("Paid $" + amount + " via UPI (" + upiId + ").");
    }

    @Override
    public String getPaymentMethod() {
        return "UPI";
    }
}
