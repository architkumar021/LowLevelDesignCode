/**
 * Driver — demonstrates Association (HAS-A, both independent).
 */
public class AssociationDemo {

    public static void main(String[] args) {
        Car car = new Car("Tesla Model 3");
        Person person = new Person("Alice", car);

        person.goForDrive();

        // Re-associate with a different car
        Car newCar = new Car("BMW i4");
        person.setCar(newCar);
        System.out.println("\n" + person.getName() + " switched cars.");
        person.goForDrive();
    }
}

/*
Expected Output:
Alice is going for a drive.
Driving a Tesla Model 3

Alice switched cars.
Alice is going for a drive.
Driving a BMW i4
*/
