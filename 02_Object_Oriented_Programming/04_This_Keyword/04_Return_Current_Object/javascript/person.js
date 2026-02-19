class Person {
    setName(name) {
        this.name = name;
        return this; // Enables method chaining
    }

    display() {
        console.log("Name: " + this.name);
    }
}

module.exports = Person;

