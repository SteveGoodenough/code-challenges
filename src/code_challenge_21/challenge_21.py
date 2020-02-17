board = []
solutions = []


def solve_sudoku(grid):
    global board
    global solutions
    solutions = []
    board = convert_list_to_board(grid)
    solve_it()
    print("solutions found:", len(solutions), solutions)
    return solutions


def solve_it():
    global board
    print('*', end='')
    for x in range(9):
        for y in range(9):
            if board[y][x] == 0:
                for num in range(1, 10):
                    if check_if_number_allowed(x, y, num):
                        board[y][x] = num
                        solve_it()
                        board[y][x] = 0
                return
    add_solution(board)


def add_solution(solution):
    global solutions
    solutions.append(convert_board_to_list(board))
    print("solution=", solution, len(solutions))


def convert_list_to_board(grid):
    return [grid[i:i+9] for i in range(0, len(grid), 9)]


def convert_board_to_list(board):
    flat_list = []
    for row in board:
        for col in row:
            flat_list.append(col)
    return flat_list


def check_if_number_allowed(x, y, num):
    global board
    for col in range(9):
        if board[y][col] == num:
            return False
    for row in range(9):
        if board[row][x] == num:
            return False
    x_square = int(x / 3) * 3
    y_square = int(y / 3) * 3
    for col_square in range(3):
        for row_square in range(3):
            if board[y_square + row_square][x_square + col_square] == num:
                return False
    return True
