#!/usr/bin/env python3

from brain_games.common import game, get_db


def main():
    db = get_db('brain_progression.json')
    game(db, 'What number is missing in the progression?')


if __name__ == "__main__":
    main()
