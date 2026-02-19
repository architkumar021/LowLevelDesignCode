/**
 * Main.java - Driver class to demonstrate Classes and Objects
 *
 * Shows:
 *   - Creating objects (instances) from a class
 *   - Invoking methods on objects
 *   - Accessing state through getters
 *   - Object behaviour influenced by internal state
 */
public class Main {

    public static void main(String[] args) {

        // ── Creating objects ────────────────────────────────────────────
        Car car1 = new Car("Toyota", "Corolla", 2021);
        Car car2 = new Car("Honda", "Civic", 2022);

        // ── Display initial info ────────────────────────────────────────
        car1.displayInfo();
        car2.displayInfo();
        System.out.println();

        // ── Start engines ───────────────────────────────────────────────
        car1.startEngine();
        car2.startEngine();
        car1.startEngine();   // trying to start again — already running
        System.out.println();

        // ── Accelerate & brake ──────────────────────────────────────────
        car1.accelerate(60);
        car1.accelerate(40);
        car1.brake(30);
        System.out.println();

        // ── Try to stop engine while moving ─────────────────────────────
        car1.stopEngine();    // should warn — still moving
        car1.brake(70);       // bring to 0
        car1.stopEngine();    // now it works
        System.out.println();

        // ── Final state ─────────────────────────────────────────────────
        car1.displayInfo();
        car2.displayInfo();
    }
}

/*
Expected Output:
────────────────
Car Info: Toyota Corolla (2021) | Engine: OFF | Speed: 0 km/h
Car Info: Honda Civic (2022) | Engine: OFF | Speed: 0 km/h

2021 Toyota Corolla → Engine started.
2022 Honda Civic → Engine started.
2021 Toyota Corolla → Engine is already running.

2021 Toyota Corolla → Accelerated to 60 km/h.
2021 Toyota Corolla → Accelerated to 100 km/h.
2021 Toyota Corolla → Braked to 70 km/h.

2021 Toyota Corolla → Cannot stop engine while moving! Current speed: 70 km/h
2021 Toyota Corolla → Braked to 0 km/h.
2021 Toyota Corolla → Engine stopped.

Car Info: Toyota Corolla (2021) | Engine: OFF | Speed: 0 km/h
Car Info: Honda Civic (2022) | Engine: ON | Speed: 0 km/h
*/
