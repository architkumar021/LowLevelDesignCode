class Example {
    constructor(a, b) {
        this.a = a;
        this.b = b;
    }
}

const example = new Example(); // No error in JS, but a and b will be undefined
console.log(example);

/*
In Java, this would cause a Compilation Error because
no default constructor exists when a parameterized constructor is defined.

In JavaScript, there is no compilation error, but a and b will be undefined.

Output:
Example { a: undefined, b: undefined }
*/

