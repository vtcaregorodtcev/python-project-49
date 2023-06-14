import random


from brain_games.common import GAME_COUNT, save_db


DB_NAME = 'brain_gcd.json'


def generate_db():
    questions = []
    answers = []
    for _ in range(GAME_COUNT):
        num1 = random.randint(1, 300)
        num2 = random.randint(1, 300)
        questions.append(f"{num1} {num2}")
        answers.append(str(gcd(num1, num2)))

    db = {"questions": questions, "answers": answers}
    save_db(db, DB_NAME)


def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


generate_db()
