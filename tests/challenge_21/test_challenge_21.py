from code_challenge_21.challenge_21 import solve_sudoku
from code_challenge_21.challenge_21 import check_if_number_allowed


def test_a_number_allowed():
    board = [
        [0, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 1, 0, 0, 0, 0],
        [3, 0, 0, 0, 2, 0, 0, 0, 0],
        [2, 0, 0, 0, 3, 0, 0, 0, 0],
        [6, 0, 0, 0, 4, 0, 0, 0, 0],
        [7, 1, 4, 0, 6, 0, 0, 5, 0],
        [8, 0, 6, 0, 7, 0, 0, 0, 0],
        [9, 3, 2, 0, 8, 0, 0, 0, 0],
    ]
    valid = check_if_number_allowed(board, 0, 0, 1)
    assert valid is True

    valid = check_if_number_allowed(board, 4, 1, 9)
    assert valid is True

    valid = check_if_number_allowed(board, 1, 7, 5)
    assert valid is True


def test_a_number_not_allowed():
    board = [
        [0, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 1, 0, 0, 0, 0],
        [3, 0, 0, 0, 2, 0, 0, 0, 0],
        [2, 0, 0, 0, 3, 0, 0, 0, 0],
        [6, 0, 0, 0, 4, 0, 0, 0, 0],
        [7, 1, 4, 0, 6, 0, 0, 0, 0],
        [8, 0, 6, 0, 7, 0, 0, 0, 0],
        [9, 3, 2, 0, 8, 0, 0, 0, 0],
    ]
    valid = check_if_number_allowed(board, 0, 0, 2)
    assert valid is False


def test_a_number_not_allowed_as_in_square():
    board = [
        [1, 2, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
    ]
    valid = check_if_number_allowed(board, 2, 1, 2)
    assert valid is False

    valid = check_if_number_allowed(board, 6, 8, 2)
    assert valid is False

    valid = check_if_number_allowed(board, 6, 8, 3)
    assert valid is False


def test_solvable_sudoku():
    grid = [
        7, 0, 9, 0, 0, 2, 6, 8, 0,
        0, 0, 2, 0, 5, 0, 7, 0, 4,
        0, 0, 0, 0, 0, 0, 2, 0, 0,
        1, 9, 0, 0, 0, 7, 0, 6, 0,
        8, 6, 7, 1, 9, 5, 0, 4, 0,
        5, 0, 4, 0, 0, 0, 0, 9, 0,
        4, 3, 5, 7, 8, 0, 0, 2, 0,
        0, 0, 6, 4, 0, 0, 0, 0, 1,
        9, 8, 0, 5, 0, 6, 0, 0, 3
    ]
    solved_grid = solve_sudoku(grid)
    print(solved_grid)
    assert solved_grid == [
        [7, 4, 9, 3, 1, 2, 6, 8, 5],
        [6, 1, 2, 9, 5, 8, 7, 3, 4],
        [3, 5, 8, 6, 7, 4, 2, 1, 9],
        [1, 9, 3, 2, 4, 7, 5, 6, 8],
        [8, 6, 7, 1, 9, 5, 3, 4, 2],
        [5, 2, 4, 8, 6, 3, 1, 9, 7],
        [4, 3, 5, 7, 8, 1, 9, 2, 6],
        [2, 7, 6, 4, 3, 9, 8, 5, 1],
        [9, 8, 1, 5, 2, 6, 4, 7, 3]
    ]
