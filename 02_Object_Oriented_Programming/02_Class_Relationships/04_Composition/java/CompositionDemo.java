/**
 * Driver — demonstrates Composition (strong HAS-A, owned lifecycle).
 *
 * The House creates its Rooms internally.
 * Rooms cannot outlive the House — if the House is destroyed, Rooms are gone.
 */
public class CompositionDemo {

    public static void main(String[] args) {
        House house = new House("123 Main Street");
        house.showHouse();
    }
}

/*
Expected Output:
House at 123 Main Street contains:
  - Living Room (350.0 sq ft)
  - Kitchen (200.0 sq ft)
  - Bedroom (300.0 sq ft)
  - Bathroom (100.0 sq ft)
  Total area: 950.0 sq ft
*/
