#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    """Convert string temperature to int."""
    return int(temp_str)


def test_temperature() -> None:
    """Test temperature input with error handling."""
    print("=== Garden Temperature ===")

    # Test valid input
    try:
        print("Input data is '25'")
        temp = input_temperature("25")
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    # Test invalid input
    try:
        print("Input data is 'abc'")
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
