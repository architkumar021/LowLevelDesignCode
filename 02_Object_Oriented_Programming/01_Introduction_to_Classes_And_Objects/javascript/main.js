/**
 * main.js - Driver script to demonstrate Classes and Objects in JavaScript
 *
 * Shows:
 *   - Creating objects (instances) from a class
 *   - Invoking methods on objects
 *   - Accessing state through getters
 *   - Object behaviour influenced by internal state
 *
 * Run:  node main.js
 */

const Car = require("./car");

// ── Creating objects ──────────────────────────────────────────────────
const car1 = new Car("Toyota", "Corolla", 2021);
const car2 = new Car("Honda", "Civic", 2022);

// ── Display initial info ──────────────────────────────────────────────
car1.displayInfo();
car2.displayInfo();
console.log();

// ── Start engines ─────────────────────────────────────────────────────
car1.startEngine();
car2.startEngine();
car1.startEngine(); // trying to start again — already running
console.log();

// ── Accelerate & brake ────────────────────────────────────────────────
car1.accelerate(60);
car1.accelerate(40);
car1.brake(30);
console.log();

// ── Try to stop engine while moving ───────────────────────────────────
car1.stopEngine(); // should warn — still moving
car1.brake(70); // bring to 0
car1.stopEngine(); // now it works
console.log();

// ── Final state ───────────────────────────────────────────────────────
car1.displayInfo();
car2.displayInfo();

/*
Expected Output:
────────────────
Car Info: Toyota Corolla (2021) | Engine: OFF | Speed: 0 km/h
Car Info: Honda Civic (2022) | Engine: OFF | Speed: 0 km/h

2021 Toyota Corolla → Engine started.
2022 Honda Civic → Engine started.
2021 Toyota Corolla → Engine is already running.

2021 Toyota Corolla → Accelerated to 60 km/h.
2021 Toyota Corolla → Accelerated to 100 km/h.
2021 Toyota Corolla → Braked to 70 km/h.

2021 Toyota Corolla → Cannot stop engine while moving! Current speed: 70 km/h
2021 Toyota Corolla → Braked to 0 km/h.
2021 Toyota Corolla → Engine stopped.

Car Info: Toyota Corolla (2021) | Engine: OFF | Speed: 0 km/h
Car Info: Honda Civic (2022) | Engine: ON | Speed: 0 km/h
*/
