/**
 * inheritance — base class (superclass) in JavaScript.
 *
 * Key concept: A Dog IS-A Animal.
 * The child class inherits fields & methods from the parent.
 */

class Animal {
  #name;

  constructor(name = "Unknown") {
    this.#name = name;
  }

  get name() {
    return this.#name;
  }

  eat() {
    console.log(`${this.#name} is eating.`);
  }

  sleep() {
    console.log(`${this.#name} is sleeping.`);
  }

  toString() {
    return `Animal(${this.#name})`;
  }
}

module.exports = Animal;
