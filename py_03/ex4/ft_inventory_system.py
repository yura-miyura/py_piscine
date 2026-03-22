#!/usr/bin/env python3

from sys import argv


class InvalidParameterError(Exception):
    pass


class Inventory:
    """
    inventory class with dictonary of quantity of items
    """
    def __init__(self) -> None:
        self.inventory: dict[str, int] = {}

    def add_item(self, item: tuple[str, int]) -> None:
        if (item[0] not in self.inventory):
            self.inventory[item[0]] = item[1]
        else:
            print(f"Redundant item '{item[0]}' - discarding")

    def show_inventory(self) -> None:
        print(f"Got inventory: {self.inventory}")

    def show_items(self) -> None:
        print(f"Item list: {self.inventory.keys()}")

    def inventory_stats(self) -> None:
        items: int = len(self.inventory)
        total_quantity: int = sum(self.inventory.values())
        smallest: tuple[str, int] = ("", 0)
        biggest: tuple[str, int] = ("", 0)
        print(f"Total quantity of the {items}: {total_quantity}")
        for key, value in self.inventory.items():
            if (smallest[0] == ""):
                smallest = (key, value)
            elif (smallest[1] > value):
                smallest = (key, value)
            if (biggest[0] == ""):
                biggest = (key, value)
            elif (biggest[1] < value):
                biggest = (key, value)
            print(f"Item {key} represents "
                  f"{round(value / total_quantity * 100, 1)}%")
        print(f"Item most abundant: {biggest[0]} "
              f"with quantity {biggest[1]}")
        print(f"Item least abundant: {smallest[0]}"
              f"with quantity {smallest[1]}")

    def update_inventory(self, name: str, quantity: int) -> None:
        self.inventory.update({name: quantity})
        print(f"Updated inventory: {self.inventory}")


def split_input(item_input: str) -> list[str]:
    item: list = item_input.split(":")
    if len(item) != 2:
        raise InvalidParameterError(f"Invalid parameter: '{item_input}'")
    return item


def quantity_convert(item: list) -> tuple[str, int]:
    try:
        quantity: int = int(item[1])
    except ValueError as e:
        raise ValueError(f"Quantity error for '{item[0]}', {e}")
    return (item[0], quantity)


def ft_inventory_system() -> None:
    input: list[str] = argv
    inventory: Inventory = Inventory()
    for item in input:
        try:
            splited: list = split_input(item)
            inventory.add_item(quantity_convert(splited))
        except (ValueError, InvalidParameterError) as e:
            print(e)
    inventory.show_inventory()
    inventory.show_items()
    inventory.inventory_stats()
    inventory.update_inventory("magic_item", 1)


if __name__ == "__main__":
    ft_inventory_system()
