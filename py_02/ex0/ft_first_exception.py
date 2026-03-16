#!/usr/bin/env python3

def check_temperature(temp_str) -> int:
    """
    Checks temperature in range 0...40 and throws an error on invalid value
    """
    try:
        temp: int = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: {temp_str} is not a valid number")
    if (temp > 40):
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")
    elif (temp < 0):
        raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    temps: list[str] = ["25", "abc", "100", "-50"]
    for temp_str in temps:
        try:
            temp_int: int = check_temperature((temp_str))
        except ValueError as e:
            print(e)
        else:
            print(f"Temperature {temp_int}°C is perfect for plants!")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
