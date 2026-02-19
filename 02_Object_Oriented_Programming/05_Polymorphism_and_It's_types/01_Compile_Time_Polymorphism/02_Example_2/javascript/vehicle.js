class Vehicle {
    // JavaScript simulates method overloading by checking argument types
    start(vehicleTypeOrId) {
        if (typeof vehicleTypeOrId === 'string') {
            console.log(`Starting a ${vehicleTypeOrId}`);
        } else if (typeof vehicleTypeOrId === 'number') {
            console.log(`Starting a vehicle with ID: ${vehicleTypeOrId}`);
        }
    }
}

module.exports = Vehicle;

