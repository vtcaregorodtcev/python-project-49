#!/usr/bin/env python3

from brain_games.common import game, get_db


def main():
    db = get_db('brain_even.json')
    game(db, 'Answer "yes" if the number is even, otherwise answer "no"')


if __name__ == "__main__":
    main()
