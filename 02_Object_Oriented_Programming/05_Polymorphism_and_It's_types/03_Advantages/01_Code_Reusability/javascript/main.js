const { Car, Bike, Truck } = require('../vehicle');

const vehicles = [new Car(), new Bike(), new Truck()];
for (const vehicle of vehicles) {
    vehicle.start(); // Polymorphic behavior
}

/*
Output:
Starting the car
Starting the bike
Starting the truck
*/

