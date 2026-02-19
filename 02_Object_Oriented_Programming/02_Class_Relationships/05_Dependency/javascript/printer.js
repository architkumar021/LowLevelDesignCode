/**
 * Dependency — Printer class in JavaScript.
 */

class Printer {
  #printerName;

  constructor(printerName) {
    this.#printerName = printerName;
  }

  get printerName() {
    return this.#printerName;
  }

  print(message) {
    console.log(`[${this.#printerName}] Printing: ${message}`);
  }

  toString() {
    return `Printer(${this.#printerName})`;
  }
}

module.exports = Printer;
