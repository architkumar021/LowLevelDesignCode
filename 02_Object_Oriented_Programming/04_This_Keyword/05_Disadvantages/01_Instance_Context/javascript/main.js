const Example = require('./example');

// Calling static method
Example.displayMessage(); // Output: undefined (no instance context)

// Creating an instance to call an instance method
const example = new Example();
example.displayInstanceMessage(); // Works fine

/*
Output:
undefined
Hello, World!
*/

