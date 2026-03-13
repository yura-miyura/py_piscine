#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, cm: int, days: int):
        self.name: str = name
        self.height: int = cm
        self.age: int = days
    def plant_info(self) -> str:
        message: str = f"\n{self.name.capitalize()} ({self.__class__.__name__}): {self.height}cm, {self.age} days"
        return (message)

class Flower(Plant):
    def __init__(self, name: str, cm: int, days: int, color: str):
        super().__init__(name, cm, days)
        self.color: str = color
    def bloom(self) -> None:
        print(f"{self.name.capitalize()} is·blooming·beautifully!")
    def plant_info(self) -> str:
        message: str = f", {self.color} color"
        return super().plant_info() + message

class Tree(Plant):
    def __init__(self, name: str, cm: int, days: int, trunk_diameter: int):
        super().__init__(name, cm, days)
        self.trunk_diameter: int = trunk_diameter
    def produce_shade(self, shade: int):
        print(f"Oak provides {shade} square meters of shade")
    def plant_info(self) -> str:
        message: str = f", {self.trunk_diameter}cm diameter"
        return super().plant_info() + message

class Vegetable(Plant):
    def __init__(self, name: str, cm: int, days: int, harvest_season: str, nutritional_value: str):
        super().__init__(name, cm, days)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value
    def plant_info(self) -> str:
        message: str = f", {self.harvest_season} harvest"
        return super().plant_info() + message
    def nutritional_message(self) -> None:
        print(f"{self.name.capitalize()} is rich in {self.nutritional_value}")



def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    rose: Flower = Flower("rose", 25, 30, "red")
    print(rose.plant_info())
    rose.bloom()

    oak: Tree= Tree("oak", 500, 1825, 50)
    print(oak.plant_info())
    oak.produce_shade(78)

    tomato: Vegetable = Vegetable("tomato", 80, 90, "summer", "vitamin C")
    print(tomato.plant_info())
    tomato.nutritional_message()


if __name__ == "__main__":
    ft_plant_types()

