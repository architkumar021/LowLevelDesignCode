class Person {
    greet(person) {
        console.log("Hello, " + person.toString());
    }

    introduce() {
        this.greet(this); // Passes the current object
    }

    toString() {
        return "I am a Person instance.";
    }
}

module.exports = Person;

