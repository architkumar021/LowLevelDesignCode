/**
 * inheritance — derived class (subclass) in JavaScript.
 *
 * Dog extends Animal → inherits eat() and sleep(),
 * and adds its own behaviour: bark().
 */

const Animal = require("./animal");

class Dog extends Animal {
  #breed;

  constructor(name, breed) {
    super(name); // call parent constructor
    this.#breed = breed;
  }

  get breed() {
    return this.#breed;
  }

  bark() {
    console.log(`${this.name} barks: Woof Woof!`);
  }

  toString() {
    return `Dog(${this.name}, breed=${this.#breed})`;
  }
}

module.exports = Dog;
