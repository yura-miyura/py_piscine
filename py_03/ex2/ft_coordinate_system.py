#!/usr/bin/env python3

from sys import argv
from math import sqrt


class TooManyArgumentsError(Exception):
    def __ini__(self):
        super().__init__("Too many arguments on an input (2 max)")


def distance_calc(t1: tuple, t2: tuple) -> None:
    x1, y1, z1 = t1
    x2, y2, z2 = t2
    x_root: int = (x2 - x1) * (x2 - x1)
    y_root: int = (y2 - y1) * (y2 - y1)
    z_root: int = (z2 - z1) * (z2 - z1)
    distance: float = sqrt(x_root + y_root + z_root)
    print(f"Distance between {t1} and {t2}: {"{:.2f}".format(distance)}")


def convert_input(input: str) -> tuple:
    input_int: list[int] = []
    input_list: list[str] = input.split(',')
    for data in input_list:
        input_int.append(int(data))
    return tuple(input_int)


def demonstration(location: tuple) -> None:
    x, y, z = location
    print("Unpacing demonstration")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"coordinates: X={x}, Y={y}, Z={z}")


def ft_coordinate_system(av: list[str]) -> None:
    av.pop(0)
    ac: int = len(av)
    start_loc: tuple
    finish_loc: tuple
    msg: str

    if (ac == 2):
        print(f"Parsing coordinares \"{av[0]}\" \"{av[1]}\"")
    elif (ac == 1):
        print(f"Parsing coordinares \"{av[0]}\"")
    if (ac == 1):
        start_loc = (0, 0, 0)
        finish_loc = convert_input(av[0])
        msg = f"Parsed position: {finish_loc}"
    elif (ac == 2):
        start_loc = convert_input(av[0])
        finish_loc = convert_input(av[1])
        msg = f"Parsed position: {start_loc} {finish_loc}"
    else:
        raise TooManyArgumentsError
    print(msg)
    distance_calc(start_loc, finish_loc)
    print()
    demonstration(finish_loc)


def test_coordinate_system() -> None:
    finish_loc: tuple
    start_loc: tuple
    loc_str: str

    start_loc = (0, 0, 0)
    finish_loc = (10, 20, 5)
    print(f"Position created: {finish_loc}")
    distance_calc(start_loc, finish_loc)
    print()
    loc_str = "3,4,0"
    print(f"Parsing coordinates: \"{loc_str}\"")
    finish_loc = convert_input(loc_str)
    print(f"Parsed position: {finish_loc}")
    distance_calc(start_loc, finish_loc)
    print()
    loc_str = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{loc_str}\"")
    try:
        convert_input(loc_str)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type {e.__class__.__name__}"
              f"Args: (\"{e.args[0]}\")")
    print()
    demonstration(finish_loc)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    av: list[str] = argv
    try:
        if (len(av) == 1):
            test_coordinate_system()
        else:
            ft_coordinate_system(av)
    except TooManyArgumentsError as e:
        print(e)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type {e.__class__.__name__}"
              f"Args: (\"{e.args[0]}\")")
    print()
