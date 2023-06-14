#!/usr/bin/env python3

from brain_games.common import game, get_db
from brain_games.games.brain_calc import DB_NAME


def main():
    db = get_db(DB_NAME)
    game(db, 'What is the result of the expression?')


if __name__ == "__main__":
    main()
