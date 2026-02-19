/**
 * Driver — demonstrates Dependency (USES-A temporarily).
 * Run: node main.js
 */

const Document = require("./document");
const Printer = require("./printer");

const doc = new Document("Report", "Hello, World!");
const officePrinter = new Printer("Office HP");
const homePrinter = new Printer("Home Canon");

// Same document, different printers — dependency is temporary
doc.printDocument(officePrinter);
console.log();
doc.printDocument(homePrinter);

/*
Expected Output:
Document: Report
[Office HP] Printing: Hello, World!

Document: Report
[Home Canon] Printing: Hello, World!
*/
