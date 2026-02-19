class Example {
    constructor(value) {
        if (value < 0) {
            console.log("Invalid value! Constructor exiting early.");
            return; // Exits the constructor early
        }
        this.value = value; // Initializes the value if valid
    }

    display() {
        console.log(`Value: ${this.value}`);
    }
}

module.exports = Example;

