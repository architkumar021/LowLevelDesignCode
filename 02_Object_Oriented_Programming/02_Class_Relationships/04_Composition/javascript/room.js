/**
 * Composition — Room class in JavaScript.
 */

class Room {
  #name;
  #areaSqFt;

  constructor(name, areaSqFt) {
    this.#name = name;
    this.#areaSqFt = areaSqFt;
  }

  get name() {
    return this.#name;
  }

  get areaSqFt() {
    return this.#areaSqFt;
  }

  toString() {
    return `${this.#name} (${this.#areaSqFt} sq ft)`;
  }
}

module.exports = Room;
