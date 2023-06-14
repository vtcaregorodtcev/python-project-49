#!/usr/bin/env python3

from brain_games.common import game, get_db
from brain_games.games.brain_prime import DB_NAME


def main():
    db = get_db(DB_NAME)
    game(db, 'Answer "yes" if given number is prime. Otherwise answer "no".')


if __name__ == "__main__":
    main()
