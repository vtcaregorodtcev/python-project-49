#!/usr/bin/env python3

import json

from brain_games.cli import game_round, welcome_user
from brain_games.tools import get_indices_for_game

with open('brain_games/db/brain_even.json') as file:
    db = json.load(file)


def main():
    if len(db['questions']) != len(db['answers']):
        print('Game is corrupted. Please fix the database.')
        return

    print("Welcome to the Brain Games!")
    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no"')

    indices = get_indices_for_game(len(db['questions']))

    for index in indices:
        question = db['questions'][index]
        correct_answer = db['answers'][index]

        answer, is_correct = game_round(question, correct_answer)

        if is_correct:
            print('Correct!')
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                answer, correct_answer))
            print("Let's try again, {0}!".format(name))
            return

    print("Congratulations, {0}!".format(name))


if __name__ == "__main__":
    main()
