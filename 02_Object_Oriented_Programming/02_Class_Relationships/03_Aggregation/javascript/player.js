/**
 * Aggregation — Player class in JavaScript.
 */

class Player {
  #name;
  #jerseyNumber;

  constructor(name, jerseyNumber) {
    this.#name = name;
    this.#jerseyNumber = jerseyNumber;
  }

  get name() {
    return this.#name;
  }

  get jerseyNumber() {
    return this.#jerseyNumber;
  }

  toString() {
    return `${this.#name} (#${this.#jerseyNumber})`;
  }
}

module.exports = Player;
