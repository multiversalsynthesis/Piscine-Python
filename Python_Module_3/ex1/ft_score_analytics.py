import sys
from typing import List


def main() -> None:
    """Process game scores from command line."""
    print("=== Player Score Analytics ===")

    if len(sys.argv) < 2:
        print(
            "No scores provided. Usage: python3 "
            + "ft_score_analytics.py <score1> <score2> ..."
        )
        return

    scores: List[float] = []
    for arg in sys.argv[1:]:
        try:
            score: float = float(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not scores:
        print(
            "No scores provided. Usage: python3 "
            + "ft_score_analytics.py <score1> <score2> ..."
        )
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
