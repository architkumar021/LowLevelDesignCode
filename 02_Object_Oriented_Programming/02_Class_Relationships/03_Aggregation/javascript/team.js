/**
 * Aggregation — Team class in JavaScript.
 *
 * A Team aggregates Players — holds references but does NOT own lifecycle.
 */

class Team {
  #teamName;
  #players;

  constructor(teamName) {
    this.#teamName = teamName;
    this.#players = [];
  }

  get teamName() {
    return this.#teamName;
  }

  get players() {
    return [...this.#players]; // return copy
  }

  addPlayer(player) {
    this.#players.push(player);
  }

  removePlayer(player) {
    const idx = this.#players.indexOf(player);
    if (idx !== -1) this.#players.splice(idx, 1);
  }

  showTeam() {
    console.log(`Team ${this.#teamName} has players:`);
    for (const p of this.#players) {
      console.log(`  - ${p}`);
    }
  }

  toString() {
    return `Team(${this.#teamName}, size=${this.#players.length})`;
  }
}

module.exports = Team;
