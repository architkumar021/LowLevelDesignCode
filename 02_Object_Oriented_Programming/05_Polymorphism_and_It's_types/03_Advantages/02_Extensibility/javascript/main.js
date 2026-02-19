const { Vehicle, Car, Bike, Truck } = require('../vehicle');

// Extensible: Add new vehicle types without changing existing code
class Bus extends Vehicle {
    start() {
        console.log("Starting the bus");
    }
}

const vehicles = [new Car(), new Bike(), new Truck(), new Bus()];
for (const vehicle of vehicles) {
    vehicle.start(); // Polymorphic behavior handles the new type seamlessly
}

/*
Output:
Starting the car
Starting the bike
Starting the truck
Starting the bus
*/

