/**
 * Driver — demonstrates Inheritance (IS-A relationship).
 * Run: node main.js
 */

const Dog = require("./dog");

const dog = new Dog("Buddy", "Golden Retriever");

dog.eat();   // inherited from Animal
dog.sleep(); // inherited from Animal
dog.bark();  // Dog-specific

console.log(`${dog}`); // toString

/*
Expected Output:
Buddy is eating.
Buddy is sleeping.
Buddy barks: Woof Woof!
Dog(Buddy, breed=Golden Retriever)
*/
