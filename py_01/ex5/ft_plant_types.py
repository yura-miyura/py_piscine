#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, cm: int, days: int):
        self.name: str = name
        self.height: int = cm
        self.age: int = days

class Flower(Plant):
    def __init__(self, name: str, cm: int, days: int, color: str):
        super().__init__(name, cm, days)
        self.color: str = color
    def bloom(self) -> None:
        print(f"{self.name.capitalize()} is·blooming·beautifully!")

class Tree(Plant):
    def __init__(self, name: str, cm: int, days: int, trunk_diameter: int):
        super().__init__(name, cm, days)
        self.trunk_diameter: int = trunk_diameter
    def produce_shade(self, shade: int):
        print(f"Oak provides {shade} square meters of shade")

class Vebetable(Plant):
    def __init__(self, name: str, cm: int, days: int, harvest_season: str, nutritional_value: str):
        super().__init__(name, cm, days)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value
