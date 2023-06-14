import random

from brain_games.common import GAME_COUNT, save_db


DB_NAME = "brain_even.json"


def generate_db():
    questions = []
    answers = []
    for _ in range(GAME_COUNT):
        number = random.randint(1, 100)
        questions.append(str(number))
        answers.append("yes" if number % 2 == 0 else "no")

    db = {"questions": questions, "answers": answers}
    save_db(db, DB_NAME)


generate_db()
