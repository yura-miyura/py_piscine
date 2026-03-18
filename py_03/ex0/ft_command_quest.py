#!/usr/bin/env python3

import sys


def print_args(ac: int, av: list) -> None:
    if ac == 0:
        return
    print_args(ac - 1, av)
    print(f"Argument {ac}: {av[ac]}")


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    av: list = sys.argv
    ac: int = len(av)
    if (ac > 1):
        if "42" in av:
            av[0] = "\\_".join(av[0].split('_'))
        print(f"Program name: {av[0]}")
        print(f"Arguments received: {ac - 1}")
        print_args(ac - 1, av)
    else:
        print("No arguments provided!")
    print(f"Total arguments: {ac}\n")


if __name__ == "__main__":
    ft_command_quest()
