#!/usr/bin/env python3

import random


from brain_games.common import GAME_COUNT, game


def generate_db():
    questions = []
    answers = []
    for _ in range(GAME_COUNT):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(['+', '-', '*'])
        question = f"{num1} {operator} {num2}"
        if operator == '+':
            answer = str(num1 + num2)
        elif operator == '-':
            answer = str(num1 - num2)
        elif operator == '*':
            answer = str(num1 * num2)
        questions.append(question)
        answers.append(answer)

    return {"questions": questions, "answers": answers}


def main():
    game(generate_db(), 'What is the result of the expression?')


if __name__ == "__main__":
    main()
