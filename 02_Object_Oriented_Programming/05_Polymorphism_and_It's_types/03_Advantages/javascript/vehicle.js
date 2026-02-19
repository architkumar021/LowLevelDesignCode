// Vehicle interface (simulated)
class Vehicle {
    start() {
        throw new Error("start() must be implemented");
    }
}

class Car extends Vehicle {
    start() {
        console.log("Starting the car");
    }
}

class Bike extends Vehicle {
    start() {
        console.log("Starting the bike");
    }
}

class Truck extends Vehicle {
    start() {
        console.log("Starting the truck");
    }
}

module.exports = { Vehicle, Car, Bike, Truck };

