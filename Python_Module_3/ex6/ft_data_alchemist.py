import random
from typing import List, Dict


def main() -> None:
    """Data alchemist with comprehensions."""
    print("=== Game Data Alchemist ===")

    # Initial list
    players: List[str] = [
        "Alice", "Bob", "Charlie",
        "Dylan", "Emma", "Gregory", "John", "Kevin", "Liam"
    ]
    print(f"Initial list of players: {players}")

    # Capitalized
    capitalized: List[str] = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {capitalized}")

    # Only already capitalized
    only_cap: List[str] = [p for p in players if p[0].isupper()]
    print(f"New list of capitalized names only: {only_cap}")

    # Score dict
    score_dict: Dict[str, int] = {
        name: random.randint(50, 1000) for name in capitalized
    }
    print(f"Score dict: {score_dict}")

    # Average
    avg: float = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {avg:.2f}")

    # High scores
    high_scores: Dict[str, int] = {
        k: v for k, v in score_dict.items() if v > avg
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
