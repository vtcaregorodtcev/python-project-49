import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,', name.strip())

    return name


def game_round(question, correct_answer):
    print('Question: ', question)
    answer = prompt.string('Your answer: ')

    return answer, answer == correct_answer
