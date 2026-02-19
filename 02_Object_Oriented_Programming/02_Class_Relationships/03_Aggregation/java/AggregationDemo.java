/**
 * Driver — demonstrates Aggregation (HAS-A with weak ownership).
 *
 * Players are created externally and added to a Team.
 * Destroying the Team does not destroy the Players.
 */
public class AggregationDemo {

    public static void main(String[] args) {
        Player p1 = new Player("Stephen", 30);
        Player p2 = new Player("Klay", 11);
        Player p3 = new Player("Draymond", 23);

        Team team = new Team("Warriors");
        team.addPlayer(p1);
        team.addPlayer(p2);
        team.addPlayer(p3);
        team.showTeam();

        // Remove a player — the player object still exists
        team.removePlayer(p2);
        System.out.println("\nAfter removing Klay:");
        team.showTeam();
        System.out.println("\nKlay still exists: " + p2);
    }
}

/*
Expected Output:
Team Warriors has players:
  - Stephen (#30)
  - Klay (#11)
  - Draymond (#23)

After removing Klay:
Team Warriors has players:
  - Stephen (#30)
  - Draymond (#23)

Klay still exists: Klay (#11)
*/
