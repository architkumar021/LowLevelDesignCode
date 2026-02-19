class Movie {
    // Parameterized constructor
    constructor(titleOrMovie, duration) {
        if (titleOrMovie instanceof Movie) {
            // Copy constructor
            this.title = titleOrMovie.title;
            this.duration = titleOrMovie.duration;
        } else {
            this.title = titleOrMovie;
            this.duration = duration;
        }
    }

    displayDetails() {
        console.log(`Title: ${this.title}, Duration: ${this.duration} mins`);
    }
}

module.exports = Movie;

