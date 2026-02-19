/**
 * Driver — demonstrates Inheritance (IS-A relationship).
 */
public class InheritanceDemo {

    public static void main(String[] args) {
        Dog dog = new Dog("Buddy", "Golden Retriever");

        dog.eat();      // inherited from Animal
        dog.sleep();    // inherited from Animal
        dog.bark();     // Dog-specific

        System.out.println(dog);  // toString
    }
}

/*
Expected Output:
Buddy is eating.
Buddy is sleeping.
Buddy barks: Woof Woof!
Dog(Buddy, breed=Golden Retriever)
*/
