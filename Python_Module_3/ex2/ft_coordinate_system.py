import math
from typing import Tuple


def get_player_pos() -> Tuple[float, float, float]:
    """Get player coordinates from user input with validation."""
    while True:
        try:
            coords_str: str = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            ).strip()
            x, y, z = map(float, coords_str.split(','))
            return (x, y, z)
        except ValueError as e:
            if "could not convert" in str(e):
                param = str(e).split("'")[-2] if "'" in str(e) else "input"
                print(f"Error on parameter '{param}': {e}")
            else:
                print("Invalid syntax")
        except Exception:
            print("Invalid syntax")


def main() -> None:
    """Main coordinate system logic."""
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1: Tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    # Distance to center
    dist_center: float = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {dist_center:.4f}")

    print("Get a second set of coordinates")
    pos2: Tuple[float, float, float] = get_player_pos()

    # Distance between points
    dist: float = math.sqrt(
        (pos2[0] - pos1[0]) ** 2
        + (pos2[1] - pos1[1]) ** 2
        + (pos2[2] - pos1[2]) ** 2
    )
    print(f"Distance between the 2 sets of coordinates: {dist:.4f}")


if __name__ == "__main__":
    main()
