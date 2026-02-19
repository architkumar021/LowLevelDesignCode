class Vehicle {
    // JavaScript simulates method overloading using default/optional parameters
    start(vehicleType, speed = null) {
        if (speed !== null) {
            console.log(`Starting a ${vehicleType} with speed: ${speed} km/h`);
        } else {
            console.log(`Starting a ${vehicleType}`);
        }
    }
}

module.exports = Vehicle;

