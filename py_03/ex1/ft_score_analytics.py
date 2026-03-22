#!/usr/bin/env python3

from sys import argv


def add_scores(scores: list) -> list[int]:
    scores.pop(0)
    scores_int: list[int] = []
    score_int: int
    for score in scores:
        try:
            score_int = int(score)
            scores_int.append(score_int)
        except ValueError:
            print(f"Invalid parameter: '{score}'")
    return scores_int


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = add_scores(argv)
    players: int = len(scores)
    if players == 0:
        print("No scores provided.",
              "Usage: python3 ft_score_analytics.py",
              "<score1> <score2> ...")
    else:
        print(f"Score processed: {scores}")
        print(f"Total players: {players}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / players}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    print()


if __name__ == "__main__":
    ft_score_analytics()
