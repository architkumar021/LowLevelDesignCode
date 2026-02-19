class Movie {
    // Parameterized constructor
    constructor(title, duration) {
        this.title = title;
        this.duration = duration;
    }

    displayDetails() {
        console.log(`Title: ${this.title}, Duration: ${this.duration} mins`);
    }
}

module.exports = Movie;

