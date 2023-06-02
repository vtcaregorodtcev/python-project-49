#!/usr/bin/env python3

import json

from brain_games.common import game, is_corrupted

with open('brain_games/db/brain_gcd.json') as file:
    db = json.load(file)


def main():
    if is_corrupted(db):
        return

    game(db, 'Find the greatest common divisor of given numbers.')


if __name__ == "__main__":
    main()
