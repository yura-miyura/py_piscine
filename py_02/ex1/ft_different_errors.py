#!/usr/bin/env python3

def garden_operations(error: str) -> None:
    """
    Function that generates errors based on the input
    """
    if error == "ValueError":
        int("abc")
    elif error == "ZeroDivisionError":
        int(10 / 0)
    elif error == "FileNotFoundError":
        open("missing.txt")
    elif error == "KeyError":
        e_d = {"some": "thing"}
        e_d["else"]


def test_error_types() -> None:
    """
    Test function that calls all the errors and catch them
    """
    print("=== Garden Error Types Demo ===")
    print()
    errors: list[str] = [
            "ValueError",
            "ZeroDivisionError",
            "FileNotFoundError",
            "KeyError"]
    for error in errors:
        print(f"Testing {error}...")
        try:
            garden_operations(error)
        except ValueError:
            print("Caught ValueError: invalid literal for int()")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e.filename}")
        except KeyError as e:
            print(f"Caught KeyError: {e}")
        print()
    print("Testing multiple errors together...")
    try:
        garden_operations(errors[1])
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
