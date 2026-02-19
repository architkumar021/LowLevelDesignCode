/**
 * Association — Car class.
 *
 * Key concept: A Person HAS-A Car (uses it, but doesn't own its lifecycle).
 * Both objects can exist independently.
 */
public class Car {

    private String model;

    public Car(String model) {
        this.model = model;
    }

    public String getModel() {
        return model;
    }

    public void drive() {
        System.out.println("Driving a " + model);
    }

    @Override
    public String toString() {
        return "Car(" + model + ")";
    }
}
