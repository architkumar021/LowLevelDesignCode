import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Aggregation — Team class.
 *
 * A Team aggregates Players — it holds references to them
 * but does NOT own their lifecycle.
 */
public class Team {

    private String teamName;
    private List<Player> players = new ArrayList<>();

    public Team(String teamName) {
        this.teamName = teamName;
    }

    public String getTeamName() {
        return teamName;
    }

    public List<Player> getPlayers() {
        return Collections.unmodifiableList(players);
    }

    public void addPlayer(Player player) {
        players.add(player);
    }

    public void removePlayer(Player player) {
        players.remove(player);
    }

    public void showTeam() {
        System.out.println("Team " + teamName + " has players:");
        for (Player p : players) {
            System.out.println("  - " + p);
        }
    }

    @Override
    public String toString() {
        return "Team(" + teamName + ", size=" + players.size() + ")";
    }
}
