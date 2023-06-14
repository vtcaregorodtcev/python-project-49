import random

from brain_games.common import GAME_COUNT, save_db


DB_NAME = 'brain_prime.json'


def generate_db():
    questions = []
    answers = []
    for _ in range(GAME_COUNT):
        number = random.randint(1, 200)
        questions.append(str(number))
        answers.append("yes" if is_prime(number) else "no")

    db =  {"questions": questions, "answers": answers}
    save_db(db, DB_NAME)


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True