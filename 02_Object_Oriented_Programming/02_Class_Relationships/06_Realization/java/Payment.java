/**
 * Realization — Payment interface.
 *
 * Key concept: Concrete classes REALIZE (implement) an interface.
 * The interface defines the contract; implementations provide the behaviour.
 */
public interface Payment {

    void pay(double amount);

    String getPaymentMethod();
}
