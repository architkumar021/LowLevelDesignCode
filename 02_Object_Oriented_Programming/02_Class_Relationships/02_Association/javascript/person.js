/**
 * Association — Person class in JavaScript.
 *
 * A Person is associated with a Car.
 * The Car is passed in from outside — Person does NOT create it.
 */

class Person {
  #name;
  #car; // Association: Person "has a" Car

  constructor(name, car) {
    this.#name = name;
    this.#car = car;
  }

  get name() {
    return this.#name;
  }

  get car() {
    return this.#car;
  }

  set car(car) {
    this.#car = car;
  }

  goForDrive() {
    console.log(`${this.#name} is going for a drive.`);
    this.#car.drive();
  }

  toString() {
    return `Person(${this.#name}, car=${this.#car})`;
  }
}

module.exports = Person;
