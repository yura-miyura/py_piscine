#!/usr/bin/env python3

class GardenError(Exception):
    """A basic error for garden problems"""


class PlantError(GardenError):
    """Error for problems with plants"""
    def __init__(self, msg='The plant is wilting!', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class WaterError(GardenError):
    """ Error for problems with watering"""
    def __init__(self, msg='Not enough water in the tank', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


def test_custom_errors() -> None:
    """
    Testing function that calls and catches all the errors
    """
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        raise PlantError
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        raise WaterError
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        raise PlantError
    except GardenError as e:
        print(f"Caught a GardenError: {e}")
    try:
        raise WaterError
    except GardenError as e:
        print(f"Caught a GardenError: {e}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
