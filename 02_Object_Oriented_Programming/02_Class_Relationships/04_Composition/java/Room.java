/**
 * Composition — Room class.
 *
 * Key concept: A House is COMPOSED OF Rooms.
 * Rooms are created and owned by the House (strong ownership).
 * If the House is destroyed, its Rooms go with it.
 */
public class Room {

    private String name;
    private double areaSqFt;

    public Room(String name, double areaSqFt) {
        this.name = name;
        this.areaSqFt = areaSqFt;
    }

    public String getName() {
        return name;
    }

    public double getAreaSqFt() {
        return areaSqFt;
    }

    @Override
    public String toString() {
        return name + " (" + areaSqFt + " sq ft)";
    }
}
