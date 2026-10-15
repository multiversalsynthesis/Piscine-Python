import sys
from typing import List


def main() -> None:
    """Display command line arguments."""
    print("=== Command Quest ===")
    program_name: str = sys.argv[0]
    print(f"Program name: {program_name}")

    args: List[str] = sys.argv[1:]
    total_args: int = len(sys.argv)

    if not args:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args)}")
        for i, arg in enumerate(args, 1):
            print(f"Argument {i}: {arg}")

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
