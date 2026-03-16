#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
    valid_plants: list[str] = ["tomato", "lettuce", "carrots"]
    try:
        for pl in plant_list:
            if pl not in valid_plants:
                raise Exception(f"Error: Cannot water {pl} - invalid plant!")
            else:
                print(f"Watering {pl}")
    except Exception as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print()
    print("Testing with error...")
    water_plants(["tomato", None])
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
