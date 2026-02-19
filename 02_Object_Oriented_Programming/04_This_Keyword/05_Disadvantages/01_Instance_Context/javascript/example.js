class Example {
    constructor() {
        this.message = "Hello, World!";
    }

    // Static method
    static displayMessage() {
        // In JavaScript, 'this' inside a static method refers to the class itself,
        // not an instance. Accessing instance properties via 'this' won't work.
        console.log(this.message); // ERROR: undefined (no instance context)
    }

    displayInstanceMessage() {
        console.log(this.message); // Valid: 'this' refers to the current instance
    }
}

module.exports = Example;

