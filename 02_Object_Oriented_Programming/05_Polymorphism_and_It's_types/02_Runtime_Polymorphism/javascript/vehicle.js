class Vehicle {
    start() {
        // Base implementation (empty)
    }
}

class Car extends Vehicle {
    start() {
        console.log("Starting a car");
    }
}

class Bike extends Vehicle {
    start() {
        console.log("Starting a bike");
    }
}

class Truck extends Vehicle {
    start() {
        console.log("Starting a truck");
    }
}

module.exports = { Vehicle, Car, Bike, Truck };

