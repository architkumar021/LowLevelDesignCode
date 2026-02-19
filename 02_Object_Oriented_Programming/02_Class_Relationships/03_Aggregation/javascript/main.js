/**
 * Driver — demonstrates Aggregation (HAS-A with weak ownership).
 * Run: node main.js
 */

const Player = require("./player");
const Team = require("./team");

const p1 = new Player("Stephen", 30);
const p2 = new Player("Klay", 11);
const p3 = new Player("Draymond", 23);

const team = new Team("Warriors");
team.addPlayer(p1);
team.addPlayer(p2);
team.addPlayer(p3);
team.showTeam();

// Remove a player — the player object still exists
team.removePlayer(p2);
console.log("\nAfter removing Klay:");
team.showTeam();
console.log(`\nKlay still exists: ${p2}`);

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
