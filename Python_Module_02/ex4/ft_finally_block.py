#!/usr/bin/env python3
"""Exercise 4: Finally Block - Always Clean Up."""


class GardenError(Exception):
    """Base error for garden problems."""

    def __init__(self, message: str = "Unknown garden error") -> None:
        """Initialize GardenError with a default message."""
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    """Error for problems with plants."""

    def __init__(self, message: str = "Unknown plant error") -> None:
        """Initialize PlantError with a default message."""
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    """Water a plant if its name is properly capitalized."""
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plant_names: list[str]) -> None:
    """Open the watering system, water plants, then always close it."""
    try:
        print("Opening watering system")
        for plant_name in plant_names:
            water_plant(plant_name)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    """Run the watering system demo with valid and invalid plant names."""
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])

    print("\nTesting invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
