import random

from brain_games.common import GAME_COUNT, save_db


DB_NAME = 'brain_progression.json'


def generate_db():
    questions = []
    answers = []
    for _ in range(GAME_COUNT):
        progression = generate_progression()
        missing_index = random.randint(0, len(progression) - 1)
        missing_number = progression[missing_index]
        progression_with_gap = replace_with_gap(progression, missing_index)
        questions.append(' '.join(progression_with_gap))
        answers.append(str(missing_number))

    db = {"questions": questions, "answers": answers}
    save_db(db, DB_NAME)


def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    progression = [str(start)]
    for _ in range(9):
        next_number = start + step
        progression.append(str(next_number))
        start = next_number
    return progression


def replace_with_gap(progression, index):
    progression_with_gap = progression.copy()
    progression_with_gap[index] = ".."
    return progression_with_gap


generate_db()
