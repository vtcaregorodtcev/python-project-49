import random


def get_indices_for_game(n):
    indices = []

    while len(indices) < 3:
        random_num = random.randint(0, n)

        if random_num not in indices:
            indices.append(random_num)

    return indices
