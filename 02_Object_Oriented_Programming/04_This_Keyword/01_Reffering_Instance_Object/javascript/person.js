class Person {
    // Constructor
    constructor(name) {
        this.name = name; // 'this' resolves conflict between instance variable and parameter
    }

    display() {
        console.log("Name: " + this.name);
    }
}

module.exports = Person;

