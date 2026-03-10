#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, cm: int, days: int):
        self.name = name
        self.cm = cm
        self.days = days

    def grow(self) -> None:
        self.cm += 1

    def age(self) -> None:
        self.days += 1

    def get_info(self) -> None:
        print(f"{(self.name).capitalize()}: {self.cm}cm, {self.days} days old")


def ft_plant_growth(time: int, name: str, cm: int, days: int) -> None:
    def display_day_info(day: int, plant: Plant) -> None:
        print(f"=== Day {day} ===")
        plant.get_info()
    day_counter = 1
    plant = Plant(name, cm, days)
    display_day_info(day_counter, plant)
    while (day_counter <= time):
        plant.grow()
        plant.age()
        day_counter += 1
    display_day_info(day_counter, plant)
    print(f"Growth this week: +{plant.cm - cm}cm")


if __name__ == "__main__":
    time = 6
    name = "rose"
    cm = 25
    days = 30
    ft_plant_growth(time, name, cm, days)
