#!/usr/bin/env python3

import random


from brain_games.common import GAME_COUNT, game


def generate_db():
    questions = []
    answers = []
    for _ in range(GAME_COUNT):
        number = random.randint(1, 200)
        questions.append(str(number))
        answers.append("yes" if is_prime(number) else "no")

    return {"questions": questions, "answers": answers}


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    game(generate_db(),
         'Answer "yes" if given number is prime. Otherwise answer "no".')


if __name__ == "__main__":
    main()
