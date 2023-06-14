#!/usr/bin/env python3

from brain_games.common import game, get_db
from brain_games.games.brain_progression import DB_NAME


def main():
    db = get_db(DB_NAME)
    game(db, 'What number is missing in the progression?')


if __name__ == "__main__":
    main()
