const Example = require('./example');

const obj1 = new Example(10); // Valid value
obj1.display();
const obj2 = new Example(-5); // Invalid value, constructor exits early
obj2.display();

/*
Output:
Value: 10
Invalid value! Constructor exiting early.
Value: undefined
*/

