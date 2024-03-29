import random

from brain_games.cli import game_round, welcome_user


GAME_COUNT = 3


def get_indices_for_game(n):
    indices = []

    while len(indices) < GAME_COUNT:
        random_num = random.randint(0, n - 1)

        if random_num not in indices:
            indices.append(random_num)

    return indices


def is_corrupted(db):
    err = 'Game is corrupted. Please fix the database.'

    if 'questions' not in db or 'answers' not in db:
        print(err)
        return True

    if len(db['questions']) < GAME_COUNT:
        print(err)
        return True

    if len(db['questions']) != len(db['answers']):
        print(err)
        return True

    return False


def game(db, welcome_message):
    print("Welcome to the Brain Games!")
    name = welcome_user()

    print(welcome_message)

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
