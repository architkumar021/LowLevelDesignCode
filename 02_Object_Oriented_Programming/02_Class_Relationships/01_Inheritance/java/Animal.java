/**
 * Inheritance — Base class (superclass).
 *
 * Key concept: A Dog IS-A Animal.
 * The child class inherits fields & methods from the parent.
 */
public class Animal {

    private String name;

    public Animal() {
        this.name = "Unknown";
    }

    public Animal(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void eat() {
        System.out.println(name + " is eating.");
    }

    public void sleep() {
        System.out.println(name + " is sleeping.");
    }

    @Override
    public String toString() {
        return "Animal(" + name + ")";
    }
}
