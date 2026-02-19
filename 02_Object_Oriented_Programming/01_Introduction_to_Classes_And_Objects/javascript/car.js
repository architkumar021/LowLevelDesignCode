/**
 * car.js - Demonstrates Classes and Objects in JavaScript (ES6+)
 *
 * Key Concepts:
 *   - ES6 class syntax with constructor
 *   - Private-like fields using # (true private fields — ES2022)
 *   - Getters and setters
 *   - Methods that operate on internal state
 *   - toString() override
 */

class Car {
  // ── Private fields (ES2022) ─────────────────────────────────────────
  #manufacturer;
  #model;
  #year;
  #engineRunning;
  #speed;

  // ── Constructor ─────────────────────────────────────────────────────
  constructor(manufacturer, model, year) {
    this.#manufacturer = manufacturer;
    this.#model = model;
    this.#year = year;
    this.#engineRunning = false;
    this.#speed = 0;
  }

  // ── Getters ─────────────────────────────────────────────────────────
  get manufacturer() {
    return this.#manufacturer;
  }

  get model() {
    return this.#model;
  }

  get year() {
    return this.#year;
  }

  get engineRunning() {
    return this.#engineRunning;
  }

  get speed() {
    return this.#speed;
  }

  // ── Setters (only where mutation makes sense) ───────────────────────
  set manufacturer(value) {
    this.#manufacturer = value;
  }

  set model(value) {
    this.#model = value;
  }

  set year(value) {
    this.#year = value;
  }

  // ── Methods ─────────────────────────────────────────────────────────
  startEngine() {
    if (this.#engineRunning) {
      console.log(`${this} → Engine is already running.`);
      return;
    }
    this.#engineRunning = true;
    console.log(`${this} → Engine started.`);
  }

  stopEngine() {
    if (!this.#engineRunning) {
      console.log(`${this} → Engine is already off.`);
      return;
    }
    if (this.#speed > 0) {
      console.log(
        `${this} → Cannot stop engine while moving! Current speed: ${this.#speed} km/h`
      );
      return;
    }
    this.#engineRunning = false;
    console.log(`${this} → Engine stopped.`);
  }

  accelerate(increment) {
    if (!this.#engineRunning) {
      console.log(`${this} → Start the engine first!`);
      return;
    }
    this.#speed += increment;
    console.log(`${this} → Accelerated to ${this.#speed} km/h.`);
  }

  brake(decrement) {
    if (this.#speed === 0) {
      console.log(`${this} → Car is already stationary.`);
      return;
    }
    this.#speed = Math.max(0, this.#speed - decrement);
    console.log(`${this} → Braked to ${this.#speed} km/h.`);
  }

  displayInfo() {
    const engineStatus = this.#engineRunning ? "ON" : "OFF";
    console.log(
      `Car Info: ${this.#manufacturer} ${this.#model} (${this.#year})` +
        ` | Engine: ${engineStatus}` +
        ` | Speed: ${this.#speed} km/h`
    );
  }

  // ── toString ────────────────────────────────────────────────────────
  toString() {
    return `${this.#year} ${this.#manufacturer} ${this.#model}`;
  }
}

module.exports = Car;
