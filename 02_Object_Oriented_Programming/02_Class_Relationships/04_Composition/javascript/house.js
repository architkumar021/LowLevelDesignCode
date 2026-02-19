/**
 * Composition — House class in JavaScript.
 *
 * A House creates and owns its Rooms internally (strong ownership).
 */

const Room = require("./room");

class House {
  #address;
  #rooms;

  constructor(address) {
    this.#address = address;
    // Rooms are created INSIDE the House — composition
    this.#rooms = [
      new Room("Living Room", 350),
      new Room("Kitchen", 200),
      new Room("Bedroom", 300),
      new Room("Bathroom", 100),
    ];
  }

  get address() {
    return this.#address;
  }

  get rooms() {
    return [...this.#rooms]; // return copy
  }

  get totalArea() {
    return this.#rooms.reduce((sum, r) => sum + r.areaSqFt, 0);
  }

  showHouse() {
    console.log(`House at ${this.#address} contains:`);
    for (const r of this.#rooms) {
      console.log(`  - ${r}`);
    }
    console.log(`  Total area: ${this.totalArea} sq ft`);
  }

  toString() {
    return `House(${this.#address}, rooms=${this.#rooms.length})`;
  }
}

module.exports = House;
