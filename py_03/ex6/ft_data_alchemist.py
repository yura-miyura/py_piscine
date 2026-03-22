#!/usr/bin/env python3

import random


def ft_data_alchemist() -> None:
    """ main function to practice comprehensions """
    names: list[str] = ['Alice',
                        'bob',
                        'Charlie',
                        'dylan',
                        'Emma',
                        'Gregory',
                        'john',
                        'kevin',
                        'Liam']
    print(f"Initial list of players: {names}")
    print("New list with all names capitalized: "
          f"{[item.capitalize() for item in names]}")
    print("New list of capitalized names only: "
          f"{[item for item in names if item == item.capitalize()]}")
    scores = {name: random.randint(1, 1000) for name in names}
    print(f"Score dict: {scores}")
    score_avg = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {score_avg}")
    bigger_then_avg = {k: v for k, v in scores.items() if v > score_avg}
    print(f"High score: {bigger_then_avg}")


if __name__ == "__main__":
    ft_data_alchemist()
