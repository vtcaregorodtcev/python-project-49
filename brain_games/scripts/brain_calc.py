#!/usr/bin/env python3

from brain_games.common import game, get_db


def main():
    db = get_db('brain_calc.json')
    game(db, 'What is the result of the expression?')


if __name__ == "__main__":
    main()
