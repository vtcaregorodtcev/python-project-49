#!/usr/bin/env python3

import random


from brain_games.common import GAME_COUNT, game


def generate_db():
    questions = []
    answers = []
    for _ in range(GAME_COUNT):
        number = random.randint(1, 100)
        questions.append(str(number))
        answers.append("yes" if number % 2 == 0 else "no")

    return {"questions": questions, "answers": answers}


def main():
    game(generate_db(), 'Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == "__main__":
    main()
