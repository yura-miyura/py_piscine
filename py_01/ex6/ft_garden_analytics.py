#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, cm: int):
        self.name = name
        self.height = cm
        self.points = 0

    def plant_message(self) -> str:
        message: str = f"- {self.name.title()}: {self.height}cm"
        return message

    def grow(self, to_grow: int):
        print(f"{self.name.title()} grew {to_grow}cm")
        self.height += to_grow


class FloweringPlant(Plant):
    def __init__(self, name: str, cm: int, color: str):
        super().__init__(name, cm)
        self.color = color
        self.blooming = False

    def bloom(self) -> None:
        self.blooming = True

    def plant_message(self) -> str:
        bloom_msg: str = "blooming"
        if not self.blooming:
            bloom_msg = "not " + bloom_msg
        msg: str = f", {self.color} flowers ({bloom_msg})"
        return super().plant_message() + msg


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, cm: int, color: str, points: int):
        super().__init__(name, cm, color)
        self.points = points

    def plant_message(self) -> str:
        return super().plant_message() + f", Prize points: {self.points}"


class Garden:
    """Garden with the owner and plants"""

    def __init__(self, owner: str):
        self.total_growth = 0
        self.owner = owner
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        print(f"Added {plant.name.title()} to {self.owner}'s garden")
        self.plants.append(plant)

    def grow_all_plants(self, to_grow: int) -> None:
        print(f"{self.owner.capitalize()} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(to_grow)
            self.total_growth += to_grow


class GardenManager:
    def __init__(self):
        self.network: dict[str, Garden] = {}

    @classmethod
    def create_garden_network(cls, *gardens: Garden) -> "GardenManager":
        network: dict[str, Garden] = {}
        for garden in gardens:
            network[garden.owner] = garden
        new_class: GardenManager = cls()
        new_class.network = network
        return new_class

    class GardenStats:
        @staticmethod
        def gdn_in_network(network: dict[str, Garden]) -> int:
            counter: int = 0
            for j in network:
                counter += 1
            return counter

        @staticmethod
        def plants_in_gdn(garden: Garden) -> None:
            print("Plants in garden:")
            for plant in garden.plants:
                print(plant.plant_message())

        @staticmethod
        def plants_stats(garden: Garden) -> None:
            counter: int = 0
            for plant in garden.plants:
                counter += 1
            print(f"Plants added: {counter}, ", end='')
            print(f"Total growth: {garden.total_growth}cm")

        @staticmethod
        def types_in_gdn(garden: Garden) -> None:
            regular: int = 0
            flowering: int = 0
            prize: int = 0
            for plant in garden.plants:
                if plant.__class__.__name__ == "Plant":
                    regular += 1
                elif plant.__class__.__name__ == "FloweringPlant":
                    flowering += 1
                else:
                    prize += 1
            print(f"Plant types: {regular} regular, ", end='')
            print(f"{flowering} flowering, {prize} prize flowers")

        @staticmethod
        def height_val(network: dict[str, Garden]) -> bool:
            for garden in network.values():
                for plant in garden.plants:
                    if plant.height < 0:
                        return False
            return True

        @staticmethod
        def gdn_scr(garden: Garden) -> int:
            garden_score: int = 0
            for plant in garden.plants:
                garden_score += plant.height
                garden_score += plant.points
            garden_score += garden.total_growth * 10
            return garden_score

    def add_plant_to_garden(self, owner: str, plant: Plant) -> None:
        if owner in self.network:
            self.network[owner].add_plant(plant)
        else:
            print("Owner doesn't exist")


def ft_garden_analytics() -> None:
    owner: str = "Alice"
    p1 = Plant("oak tree", 100)
    p2 = FloweringPlant("rose", 25, "red")
    p2.bloom()
    p3 = PrizeFlower("sunflower", 50, "yellow", 10)
    p3.bloom()
    bob_garden = Garden("Bob")
    bob_garden.add_plant(Plant("apple tree", 92))

    print("=== Garden Management System Demo ===")
    print()
    # Created garden network with Alice's empty and Bob's ready garden
    garden_manager = GardenManager.create_garden_network(
            Garden(owner),
            bob_garden
            )
    # Added plants to Alice's garden
    garden_manager.add_plant_to_garden(owner, p1)
    garden_manager.add_plant_to_garden(owner, p2)
    garden_manager.add_plant_to_garden(owner, p3)
    print()
    # Grow all plants in Alice's garden by 1cm
    garden_manager.network[owner].grow_all_plants(1)
    print()
    print(f"=== {owner}'s Garden Report ===")
    al_garden: Garden = garden_manager.network[owner]
    GardenManager.GardenStats.plants_in_gdn(al_garden)
    print()
    GardenManager.GardenStats.plants_stats(al_garden)
    GardenManager.GardenStats.types_in_gdn(al_garden)
    print()
    print(f"Height validation test: {
          GardenManager.GardenStats.height_val(garden_manager.network)
          }")
    print(f"Garden scores - {owner}: {
          GardenManager.GardenStats.gdn_scr(al_garden)
          }, Bob: {
          GardenManager.GardenStats.gdn_scr(bob_garden)
          }")
    print(f"Total gardens managed: {
          GardenManager.GardenStats.gdn_in_network(garden_manager.network)
          }")


if __name__ == "__main__":
    ft_garden_analytics()
