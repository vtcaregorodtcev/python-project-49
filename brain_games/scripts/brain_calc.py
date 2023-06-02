#!/usr/bin/env python3

import json

from brain_games.common import game, get_db_path, is_corrupted

with open(get_db_path('brain_calc.json')) as file:
    db = json.load(file)


def main():
    if is_corrupted(db):
        return

    game(db, 'What is the result of the expression?')


if __name__ == "__main__":
    main()
