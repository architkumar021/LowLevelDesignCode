/**
 * Driver — demonstrates Association (HAS-A, both independent).
 * Run: node main.js
 */

const Car = require("./car");
const Person = require("./person");

const car = new Car("Tesla Model 3");
const person = new Person("Alice", car);

person.goForDrive();

// Re-associate with a different car
const newCar = new Car("BMW i4");
person.car = newCar;
console.log(`\n${person.name} switched cars.`);
person.goForDrive();

/*
Expected Output:
Alice is going for a drive.
Driving a Tesla Model 3

Alice switched cars.
Alice is going for a drive.
Driving a BMW i4
*/
