const { Car, Bike, Truck } = require('../vehicle');

let vehicle;

// Flexible: Dynamically assign different types of vehicles
vehicle = new Car();
vehicle.start(); // Output: Starting the car

vehicle = new Bike();
vehicle.start(); // Output: Starting the bike

vehicle = new Truck();
vehicle.start(); // Output: Starting the truck

/*
Output:
Starting the car
Starting the bike
Starting the truck
*/

