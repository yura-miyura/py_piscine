#!/usr/bin/env python3
import random


def gen_player_achievements() -> set:
    """ Generates random set of achivements """
    new_set: set = set()
    achivemnt_pull: list = ['Crafting Genius',
                            'Strategist',
                            'World Savior',
                            'Speed Runner',
                            'Survivor',
                            'Master Explorer',
                            'Treasure Hunter',
                            'Unstoppable',
                            'First Steps',
                            'Collector Supreme',
                            'Untouchable',
                            'Sharp Mind',
                            'Boss Slayer']
    for n in range(random.randint(0, len(achivemnt_pull))):
        new_set.add(random.choice(achivemnt_pull))
    return new_set


def ft_achievement_analytics(players: dict[str, set]) -> None:
    """
    Analytics function, reusable for any amount of players and achievements
    """
    first_set: set = set()
    for key in players.keys():
        first_set = players[key]
        break
    for key, value in players.items():
        print(f"Player {key.capitalize()}: {value}")
    print()
    print(f"All distinct achievements: {first_set.union(*players.values())}")
    print()
    print(f"Common achievements: {first_set.intersection(*players.values())}")
    print()
    cpy_players: dict[str, set]
    cpy_player: set
    for key in players.keys():
        cpy_players = players.copy()
        cpy_player = players[key]
        cpy_players.pop(key)
        print(f"Only {key.capitalize()} has: "
              f"{cpy_player.difference(*cpy_players.values())}")
    print()
    for key in players.keys():
        cpy_players = players.copy()
        cpy_player = players[key]
        cpy_players.pop(key)
        print(f"{key.capitalize()} is missing: "
              f"{(first_set.union(*players.values())).difference(cpy_player)}")


if __name__ == "__main__":
    version: str = input("Type \"d\" for default players: ")
    players: dict[str, set] = {}
    print("=== Achievement Tracker System ===")
    print()
    players["alice"] = gen_player_achievements()
    players["bob"] = gen_player_achievements()
    players["charlie"] = gen_player_achievements()
    players["dylan"] = gen_player_achievements()
    if (version == "d"):
        players["alice"] = {'Crafting Genius',
                            'World Savior',
                            'Master Explorer',
                            'Collector Supreme',
                            'Untouchable',
                            'Boss Slayer'}
        players["bob"] = {'Crafting Genius',
                          'Strategist',
                          'World Savior',
                          'Master Explorer',
                          'Unstoppable',
                          'Collector Supreme',
                          'Untouchable'}
        players["charlie"] = {'Strategist',
                              'Speed Runner',
                              'Survivor',
                              'Master Explorer',
                              'Treasure Hunter',
                              'First Steps',
                              'Collector Supreme',
                              'Untouchable',
                              'Sharp Mind'}
        players["dylan"] = {'Strategist',
                            'Speed Runner',
                            'Unstoppable',
                            'Untouchable',
                            'Boss Slayer'}
    ft_achievement_analytics(players)
