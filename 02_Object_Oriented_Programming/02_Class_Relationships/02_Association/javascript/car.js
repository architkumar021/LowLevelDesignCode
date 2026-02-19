/**
 * Association — Car class in JavaScript.
 */

class Car {
  #model;

  constructor(model) {
    this.#model = model;
  }

  get model() {
    return this.#model;
  }

  drive() {
    console.log(`Driving a ${this.#model}`);
  }

  toString() {
    return `Car(${this.#model})`;
  }
}

module.exports = Car;
