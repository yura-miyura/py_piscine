#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class SunlightError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water: int, sun: int):
        self.name = name
        self.water = water
        self.sun = sun

    def water_plant(self, liters: int) -> None:
        self.water += liters
        print(f"Watering {self.name} - success")


class GardenManager:
    def __init__(self, water: int) -> None:
        self.tank_water = water
        self.garden = []
        self.errors = []

    def add_plant(self, plant: Plant) -> None:
        """ Adds plant to garden list"""
        try:
            if (plant.name == ""):
                raise PlantError("Plant name cannot be empty!")
            self.garden.append(plant)
        except PlantError as e:
            print(f"Error adding plant: {e}")
        else:
            print(f"Added {plant.name} successfully")

    def water_plants(self, liters: int) -> None:
        """ Waters plants in the garden """
        if (self.tank_water - liters >= 0):
            print("Opening watering system")
        try:
            for plant in self.garden:
                self.tank_water -= liters
                if (self.tank_water < 0):
                    raise GardenError("Not enough water in tank")
                plant.water_plant(liters)
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            if (self.tank_water < 0):
                self.tank_water += liters
            else:
                print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(plant: Plant) -> str:
        """ Checks plant health """
        sun_msg: str = "Sunlight hours"
        msg: str = f"Error checking {plant.name}: "
        if (plant.name == ""):
            raise PlantError("Plant name cannot be empty!")
        elif (plant.water > 10):
            raise WaterError(msg +
                             f"Water level {plant.water} is too high (max 10)")
        elif (plant.water < 1):
            raise WaterError(msg +
                             f"Water level {plant.water} is too low (min 1)")
        elif (plant.sun > 12):
            raise SunlightError(msg + sun_msg +
                                f" {plant.sun} is too high (max 12)")
        elif (plant.sun < 2):
            raise SunlightError(msg + sun_msg +
                                f" {plant.sun} is too low (min 2)")
        final_msg: str = ""
        final_msg += plant.name
        return (f": healthy (water: {plant.water}, sun: {plant.sun})")

    def check_garden_health(self) -> None:
        """ Checks garden plants"""
        print("Checking plant health")
        try:
            for plant in self.garden:
                print(GardenManager.check_plant_health(plant))
        except GardenError as e:
            print(e)


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    print()
    garden_manager: GardenManager = GardenManager(10)
    print("Adding plants to garden...")
    garden_manager.add_plant(Plant("tomato", 5, 8))
    garden_manager.add_plant(Plant("lettuce", 10, 5))
    garden_manager.add_plant(Plant("", 5, 5))
    print()
    print("Watering plants...")
    garden_manager.water_plants(5)
    print()
    garden_manager.check_garden_health()
    print()
    print("Testing error recovery...")
    garden_manager.water_plants(5)
    print("System recovered and continuing...")
    print()
    print("Garden managment system test completed!")


if __name__ == "__main__":
    test_garden_management()
