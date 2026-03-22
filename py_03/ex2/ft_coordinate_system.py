#!/usr/bin/env python3

from math import sqrt


def distance_calc(t1: tuple, t2: tuple) -> float:
    """
    Calculates distance btw two coordinates x, y, z
    """
    x1, y1, z1 = t1
    x2, y2, z2 = t2
    x_root: int = (x2 - x1) * (x2 - x1)
    y_root: int = (y2 - y1) * (y2 - y1)
    z_root: int = (z2 - z1) * (z2 - z1)
    distance: float = sqrt(x_root + y_root + z_root)
    return (round(distance, 4))


def get_player_pos() -> tuple[float]:
    """
    Takes an input to creates tuple of coordinates
    """
    input_msg: str = "Enter new coordinates as floats in format 'x,y,z': "
    output_data: list = []
    while (1):
        input_pos: list[str] = input(input_msg).split(',')
        if (len(input_pos) == 3):
            try:
                for data in input_pos:
                    try:
                        output_data.append(float(data))
                    except ValueError as e:
                        output_data.clear()
                        raise ValueError(f"Error on parameter '{data}': {e}")
                break
            except ValueError as e:
                print(e)
        else:
            print("Invalid syntax")
    return tuple(output_data)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    center: tuple = (0, 0, 0)
    print("Get a first set of coordinates")
    p1: tuple = get_player_pos()
    print(f"Got a first tuple: {p1}")
    x, y, z = p1
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print(f"Distance to center: {distance_calc(center, p1)}")
    print()
    print("Get a second set of coordinates")
    p2: tuple = get_player_pos()
    print("Distance between the 2 set of coordinates "
          f"{distance_calc(p1, p2)}")
    print()
