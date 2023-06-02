#!/usr/bin/env python3

from brain_games.common import game, get_db


def main():
    db = get_db('brain_gcd.json')
    game(db, 'Find the greatest common divisor of given numbers.')


if __name__ == "__main__":
    main()
