/**
 * Aggregation — Player class.
 *
 * Key concept: A Team HAS Players, but Players can exist independently.
 * If the Team is destroyed, Players still exist (weak ownership).
 */
public class Player {

    private String name;
    private int jerseyNumber;

    public Player(String name, int jerseyNumber) {
        this.name = name;
        this.jerseyNumber = jerseyNumber;
    }

    public String getName() {
        return name;
    }

    public int getJerseyNumber() {
        return jerseyNumber;
    }

    @Override
    public String toString() {
        return name + " (#" + jerseyNumber + ")";
    }
}
