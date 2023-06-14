#!/usr/bin/env python3

from brain_games.common import game, get_db


def main():
    db = get_db('brain_prime.json')
    game(db, 'Answer "yes" if given number is prime. Otherwise answer "no".')


if __name__ == "__main__":
    main()
