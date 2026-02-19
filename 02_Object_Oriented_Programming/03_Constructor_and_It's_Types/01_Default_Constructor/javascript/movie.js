class Movie {
    // Custom default constructor
    constructor() {
        this.title = "Untitled"; // Default: "Untitled"
        this.duration = 90;      // Default: 90
    }

    displayDetails() {
        console.log(`Title: ${this.title}, Duration: ${this.duration} mins`);
    }
}

module.exports = Movie;

