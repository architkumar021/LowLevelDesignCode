const Person = require('./person');

const p = new Person();
p.setName("Bob").display(); // Method chaining enabled by returning 'this'

/*
Output:
Name: Bob
*/

