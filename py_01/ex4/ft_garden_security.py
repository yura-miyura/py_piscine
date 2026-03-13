#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, cm: int, days: int):
        self.name = name
        self.__height = cm
        self.__age = days
        self.__created()

    def __created(self) -> None:
        print(f"Plant created: {self.name.capitalize()}")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def __security_message(self, nb: int, tp: str) -> None:
        print(f"\nInvalid operation attempted: {tp} {nb}cm [REJECTED]")
        print(f"Security: Negative {tp} rejected\n")

    def set_height(self, new_height: int) -> None:
        if (new_height > 0 and new_height >= self.__height):
            self.__height = new_height
            print(f"Height updated: {new_height}cm [OK]")
            return
        self.__security_message(new_height, "height")

    def set_age(self, new_age) -> None:
        if (new_age > 0 and new_age >= self.__age):
            self.__age = new_age
            print(f"Age updated: {new_age} days [OK]")
            return
        self.__security_message(new_age, "age")

    def current_status(self) -> None:
        print(f"Current plant: {
              self.name.capitalize()
              } ({self.__height}cm, {self.__age} days)")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = Plant("rose", 1, 5)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    plant.current_status()


if __name__ == "__main__":
    ft_garden_security()
