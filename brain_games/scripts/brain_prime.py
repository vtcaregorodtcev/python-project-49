#!/usr/bin/env python3

import json

from brain_games.common import game, is_corrupted

with open('brain_games/db/brain_prime.json') as file:
    db = json.load(file)


def main():
    if is_corrupted(db):
        return

    game(db, 'Answer "yes" if given number is prime. Otherwise answer "no".')
    

if __name__ == "__main__":
    main()
