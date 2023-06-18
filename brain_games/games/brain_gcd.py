#!/usr/bin/env python3

import random


from brain_games.common import GAME_COUNT, game


def generate_db():
    questions = []
    answers = []
    for _ in range(GAME_COUNT):
        num1 = random.randint(1, 300)
        num2 = random.randint(1, 300)
        questions.append(f"{num1} {num2}")
        answers.append(str(gcd(num1, num2)))

    return {"questions": questions, "answers": answers}


def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


def main():
    game(generate_db(), 'Find the greatest common divisor of given numbers.')


if __name__ == "__main__":
    main()
