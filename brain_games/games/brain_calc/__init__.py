import random

from brain_games.common import GAME_COUNT, save_db


DB_NAME = 'brain_calc.json'

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

    db = {"questions": questions, "answers": answers}
    save_db(db, DB_NAME)

generate_db()