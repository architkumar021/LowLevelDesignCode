const { Car } = require('../vehicle');

const startTime = process.hrtime.bigint();

// Dynamic method dispatch
const myVehicle = new Car();
myVehicle.start(); // Runtime resolves method implementation dynamically

const endTime = process.hrtime.bigint();
console.log(`Time taken for method dispatch: ${endTime - startTime} nanoseconds`);

/*
Output:
Starting a car
Time taken for method dispatch: XXXXX nanoseconds
*/

