#!/usr/bin/env python3


class TemperatureError(Exception):
    """Custom exception for temperature out of range."""
    pass


def input_temperature(temp_str: str) -> int:
    """Convert string to int and validate plant temperature range."""
    try:
        temp = int(temp_str)
        if temp < 0:
            raise TemperatureError(
                f"{temp}°C is too cold for plants (min 0°C)"
            )
        if temp > 40:
            raise TemperatureError(
                f"{temp}°C is too hot for plants (max 40°C)"
            )
        return temp
    except ValueError as e:
        raise ValueError(
            f"invalid literal for int() with base 10: '{temp_str}'"
        ) from e


def test_temperature() -> None:
    """Test temperature validation with different cases."""
    print("=== Garden Temperature Checker ===")
    tests = ["25", "abc", "100", "-50"]

    for data in tests:
        print(f"Input data is '{data}'")
        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
