#!/usr/bin/env python3
def garden_operations(operation_number: int) -> str:
    """Simulate different types of errors based on operation number."""
    if operation_number == 0:
        return int("abc")  # ValueError
    elif operation_number == 1:
        return 10 // 0     # ZeroDivisionError
    elif operation_number == 2:
        with open("/non/existent/file", "r"):
            pass
    elif operation_number == 3:
        return "hello" + 42  # TypeError
    else:
        return "Operation completed successfully"


def test_error_types() -> None:
    """Test different error types."""
    print("=== Garden Error Types Demo ===")

    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            result = garden_operations(i)
            print(result)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        except Exception as e:
            print(f"Caught unexpected error: {e}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
