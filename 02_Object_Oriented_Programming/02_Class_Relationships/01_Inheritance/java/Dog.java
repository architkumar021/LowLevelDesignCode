/**
 * Inheritance — Derived class (subclass).
 *
 * Dog extends Animal → inherits eat() and sleep(),
 * and adds its own behaviour: bark().
 */
public class Dog extends Animal {

    private String breed;

    public Dog(String name, String breed) {
        super(name);    // call parent constructor
        this.breed = breed;
    }

    public String getBreed() {
        return breed;
    }

    public void bark() {
        System.out.println(getName() + " barks: Woof Woof!");
    }

    @Override
    public String toString() {
        return "Dog(" + getName() + ", breed=" + breed + ")";
    }
}
