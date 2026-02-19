class Person {
    // JavaScript doesn't support multiple constructors directly,
    // so we simulate constructor chaining with default parameters
    constructor(name, age = 0) {
        this.name = name;
        this.age = age;
    }

    display() {
        console.log("Name: " + this.name + ", Age: " + this.age);
    }
}

module.exports = Person;

