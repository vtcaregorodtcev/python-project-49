#!/usr/bin/env python3

from brain_games.common import game, get_db
from brain_games.games.brain_even import DB_NAME


def main():
    db = get_db(DB_NAME)
    game(db, 'Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == "__main__":
    main()
