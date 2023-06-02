from brain_games.common import get_indices_for_game, is_corrupted

def test_get_indices_for_game():
    n = 10
    indices = get_indices_for_game(n)

    assert len(indices) == 3
    assert all(0 <= i < n for i in indices)

def test_is_corrupted_true():
    db = {}

    is_corrupted_flag = is_corrupted(db)
    assert is_corrupted_flag == True

    db = {
        "questions": []
    }

    is_corrupted_flag = is_corrupted(db)
    assert is_corrupted_flag == True

    db = {
        "questions": [1, 2, 3],
        "answers": [1]
    }

    is_corrupted_flag = is_corrupted(db)
    assert is_corrupted_flag == True

def test_is_corrupted_false():
    db = {
        "questions": [1, 2, 3],
        "answers": [1, 2, 4]
    }

    is_corrupted_flag = is_corrupted(db)
    assert is_corrupted_flag == False