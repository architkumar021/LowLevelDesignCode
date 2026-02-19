import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Composition — House class.
 *
 * A House creates and owns its Rooms internally (strong ownership).
 * Rooms cannot exist without the House.
 */
public class House {

    private String address;
    private List<Room> rooms;

    public House(String address) {
        this.address = address;
        // Rooms are created INSIDE the House — composition
        this.rooms = new ArrayList<>();
        this.rooms.add(new Room("Living Room", 350));
        this.rooms.add(new Room("Kitchen", 200));
        this.rooms.add(new Room("Bedroom", 300));
        this.rooms.add(new Room("Bathroom", 100));
    }

    public String getAddress() {
        return address;
    }

    public List<Room> getRooms() {
        return Collections.unmodifiableList(rooms);
    }

    public double getTotalArea() {
        double total = 0;
        for (Room r : rooms) {
            total += r.getAreaSqFt();
        }
        return total;
    }

    public void showHouse() {
        System.out.println("House at " + address + " contains:");
        for (Room r : rooms) {
            System.out.println("  - " + r);
        }
        System.out.println("  Total area: " + getTotalArea() + " sq ft");
    }

    @Override
    public String toString() {
        return "House(" + address + ", rooms=" + rooms.size() + ")";
    }
}
