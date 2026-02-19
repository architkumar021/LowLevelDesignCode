const Singleton = require('./singleton');

const s1 = Singleton.getInstance();
const s2 = Singleton.getInstance();
console.log(s1 === s2); // Output: true, as both references point to the same instance

/*
Output:
true
*/

