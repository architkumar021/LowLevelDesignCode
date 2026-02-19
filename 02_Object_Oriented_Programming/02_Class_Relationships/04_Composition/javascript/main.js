/**
 * Driver — demonstrates Composition (strong HAS-A, owned lifecycle).
 * Run: node main.js
 */

const House = require("./house");

const house = new House("123 Main Street");
house.showHouse();

/*
Expected Output:
House at 123 Main Street contains:
  - Living Room (350 sq ft)
  - Kitchen (200 sq ft)
  - Bedroom (300 sq ft)
  - Bathroom (100 sq ft)
  Total area: 950 sq ft
*/
