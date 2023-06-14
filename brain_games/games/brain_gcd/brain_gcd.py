#!/usr/bin/env python3

from brain_games.common import game, get_db
from brain_games.games.brain_gcd import DB_NAME


def main():
    db = get_db(DB_NAME)
    game(db, 'Find the greatest common divisor of given numbers.')


if __name__ == "__main__":
    main()
