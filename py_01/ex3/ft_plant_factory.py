#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, cm: int, days: int):
        self.name = name
        self.cm = cm
        self.days = days


def ft_plant_factory() -> None:
    plants = [Plant("rose", 25, 30)]
    counter = 0
    plants.append(Plant("oak", 200, 365))
    plants.append(Plant("cactus", 5, 90))
    plants.append(Plant("sunflower", 80, 45))
    plants.append(Plant("fern", 15, 120))
    print("=== Plant Factory Output ===")
    for plant in plants:
        counter += 1
        print(f"Created: {
              plant.name.capitalize()
              } ({plant.cm}cm, {plant.days} days)")
    print(f"\nTotal plants created: {counter}")


if __name__ == "__main__":
    ft_plant_factory()
