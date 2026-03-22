#!/usr/bin/env python3

from typing import Generator
import random


def gen_event(names: list[str], actions: list[str]) -> Generator:
    while (True):
        yield (random.choice(names), random.choice(actions))


def consume_event(events_list: list) -> Generator:
    while events_list:
        index: int = random.randrange(len(events_list))
        yield events_list.pop(index)


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    names: list = ["bob", "alice", "dylan", "charlie"]
    actions: list = ["run", "eat", "sleep", "grab", "move", "climb", "swim"]
    for i in range(1000):
        event: tuple[str, str] = next(gen_event(names, actions))
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    events: list[tuple] = []
    for i in range(10):
        events.append(next(gen_event(names, actions)))
    print(f"Bullet list of 10 events {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    ft_data_stream()
