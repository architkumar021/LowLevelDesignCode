const { Vehicle, Car, Bike, Truck } = require('../vehicle');

// List containing various types of vehicles
const vehicleList = [new Car(), new Bike(), new Truck(), new Vehicle()];

// Debugging challenge: What type of vehicle is being started?
for (const vehicle of vehicleList) {
    vehicle.start(); // Runtime determines which start() method is called
}

/*
Output:
Starting a car
Starting a bike
Starting a truck
Starting a generic vehicle
*/

