const Movie = require('./movie');

const original = new Movie("Inception", 148);
const copy = new Movie(original); // Copy constructor is called
copy.displayDetails();

/*
Output:
Title: Inception, Duration: 148 mins
*/

