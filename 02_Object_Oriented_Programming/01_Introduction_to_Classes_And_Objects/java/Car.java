/**
 * Car.java - Demonstrates Classes and Objects in Java
 *
 * Key Concepts:
 *   - Class definition with attributes (fields) and methods
 *   - Constructor for initialising object state
 *   - Encapsulation via private fields + public getters/setters
 *   - Method behaviour tied to object state
 *   - Overriding toString() for readable output
 */
public class Car {

    // ── Attributes (private for encapsulation) ──────────────────────────
    private String manufacturer;
    private String model;
    private int year;
    private boolean engineRunning;
    private int speed; // km/h

    // ── Constructor ─────────────────────────────────────────────────────
    public Car(String manufacturer, String model, int year) {
        this.manufacturer = manufacturer;
        this.model = model;
        this.year = year;
        this.engineRunning = false;
        this.speed = 0;
    }

    // ── Getters ─────────────────────────────────────────────────────────
    public String getManufacturer() {
        return manufacturer;
    }

    public String getModel() {
        return model;
    }

    public int getYear() {
        return year;
    }

    public boolean isEngineRunning() {
        return engineRunning;
    }

    public int getSpeed() {
        return speed;
    }

    // ── Setters (only where mutation makes sense) ───────────────────────
    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public void setYear(int year) {
        this.year = year;
    }

    // ── Behaviours / Methods ────────────────────────────────────────────
    public void startEngine() {
        if (engineRunning) {
            System.out.println(this + " → Engine is already running.");
            return;
        }
        engineRunning = true;
        System.out.println(this + " → Engine started.");
    }

    public void stopEngine() {
        if (!engineRunning) {
            System.out.println(this + " → Engine is already off.");
            return;
        }
        if (speed > 0) {
            System.out.println(this + " → Cannot stop engine while moving! Current speed: " + speed + " km/h");
            return;
        }
        engineRunning = false;
        System.out.println(this + " → Engine stopped.");
    }

    public void accelerate(int increment) {
        if (!engineRunning) {
            System.out.println(this + " → Start the engine first!");
            return;
        }
        speed += increment;
        System.out.println(this + " → Accelerated to " + speed + " km/h.");
    }

    public void brake(int decrement) {
        if (speed == 0) {
            System.out.println(this + " → Car is already stationary.");
            return;
        }
        speed = Math.max(0, speed - decrement);
        System.out.println(this + " → Braked to " + speed + " km/h.");
    }

    public void displayInfo() {
        System.out.println("Car Info: " + manufacturer + " " + model + " (" + year + ")"
                + " | Engine: " + (engineRunning ? "ON" : "OFF")
                + " | Speed: " + speed + " km/h");
    }

    // ── toString ────────────────────────────────────────────────────────
    @Override
    public String toString() {
        return year + " " + manufacturer + " " + model;
    }
}
