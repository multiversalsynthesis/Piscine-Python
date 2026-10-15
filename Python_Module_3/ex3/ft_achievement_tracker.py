import random
from typing import Set, List, Dict


def gen_player_achievements(achievements: List[str]) -> Set[str]:
    """Generate random achievements for a player."""
    num_ach: int = random.randint(3, 8)
    return set(random.sample(achievements, num_ach))


def main() -> None:
    """Achievement tracker main logic."""
    print("=== Achievement Tracker System ===")

    all_achievements: List[str] = [
        "Crafting Genius", "World Savior",
        "Master Explorer", "Collector Supreme",
        "Untouchable", "Boss Slayer", "Strategist", "Survivor", "Speed Runner",
        "Treasure Hunter", "First Steps", "Sharp Mind", "Hidden Path Finder",
    ]

    players: List[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    player_achs: Dict[str, Set[str]] = {}

    for player in players:
        player_achs[player] = gen_player_achievements(all_achievements)
        print(f"Player {player}: {sorted(player_achs[player])}")

    # All unique
    all_unique: Set[str] = set.union(*player_achs.values())
    print(f"\nAll distinct achievements: {sorted(all_unique)}")

    # Common to all
    common: Set[str] = set.intersection(*player_achs.values())
    print(f"Common achievements: {sorted(common)}")

    # Unique per player and missing
    for player, achs in player_achs.items():
        # Build set of all other players' achievements
        other_achs: Set[str] = set()
        for p, s in player_achs.items():
            if p != player:
                other_achs = other_achs.union(s)

        only_mine: Set[str] = achs.difference(other_achs)
        print(f"Only {player} has: {sorted(only_mine)}")

        missing: Set[str] = all_unique - achs
        print(f"{player} is missing: {sorted(missing)}")


if __name__ == "__main__":
    main()
