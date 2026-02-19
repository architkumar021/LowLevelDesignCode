/**
 * Association — Person class.
 *
 * A Person is associated with a Car.
 * The Car is passed in from outside — Person does NOT create it.
 * Both can exist independently.
 */
public class Person {

    private String name;
    private Car car;  // Association: Person "has a" Car

    public Person(String name, Car car) {
        this.name = name;
        this.car = car;
    }

    public String getName() {
        return name;
    }

    public Car getCar() {
        return car;
    }

    public void setCar(Car car) {
        this.car = car;
    }

    public void goForDrive() {
        System.out.println(name + " is going for a drive.");
        car.drive();
    }

    @Override
    public String toString() {
        return "Person(" + name + ", car=" + car + ")";
    }
}
