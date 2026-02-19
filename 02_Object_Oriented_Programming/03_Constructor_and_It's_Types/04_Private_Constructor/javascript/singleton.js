class Singleton {
    static #instance = null;

    // Private constructor (simulated via static method)
    constructor() {
        if (Singleton.#instance) {
            throw new Error("Use Singleton.getInstance() instead of new Singleton()");
        }
    }

    static getInstance() {
        if (!Singleton.#instance) {
            Singleton.#instance = new Singleton();
        }
        return Singleton.#instance;
    }
}

module.exports = Singleton;

