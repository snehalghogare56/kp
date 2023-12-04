54, 69) CSP for sodoku game
Csp: from constraint import Problem, AllDifferentConstraint

def create_sudoku_csp(board):
    problem = Problem()

    # Add variables for each cell
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                problem.addVariable(f"cell_{i}_{j}", range(1, 10))

    # Add constraints for rows, columns, and 3x3 subgrids
    for i in range(9):
        # Row constraint
        problem.addConstraint(AllDifferentConstraint(), [f"cell_{i}_{j}" for j in range(9)])

        # Column constraint
        problem.addConstraint(AllDifferentConstraint(), [f"cell_{j}_{i}" for j in range(9)])

    # Subgrid constraint
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            problem.addConstraint(AllDifferentConstraint(), [f"cell_{x}_{y}" for x in range(i, i + 3) for y in range(j, j + 3)])

    # Add initial assignments as constraints
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                problem.addConstraint(lambda value, i=i, j=j: value == board[i][j], (f"cell_{i}_{j}",))

    return problem

def solve_sudoku(board):
    csp = create_sudoku_csp(board)
    solution = csp.getSolution()
    return solution

def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    # Example Sudoku board (0 represents empty cells)
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Initial Sudoku Board:")
    print_sudoku(sudoku_board)

    solution = solve_sudoku(sudoku_board)

    if solution:
        print("\nSolved Sudoku:")
        solved_board = [[solution[f"cell_{i}_{j}"] for j in range(9)] for i in range(9)]
        print_sudoku(solved_board)
    else:
        print("\nNo solution found.")
user input: from constraint import Problem, AllDifferentConstraint

def create_sudoku_csp(board):
    problem = Problem()

    # Add variables for each cell
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                problem.addVariable(f"cell_{i}_{j}", range(1, 10))

    # Add constraints for rows, columns, and 3x3 subgrids
    for i in range(9):
        # Row constraint
        problem.addConstraint(AllDifferentConstraint(), [f"cell_{i}_{j}" for j in range(9)])

        # Column constraint
        problem.addConstraint(AllDifferentConstraint(), [f"cell_{j}_{i}" for j in range(9)])

    # Subgrid constraint
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            problem.addConstraint(AllDifferentConstraint(), [f"cell_{x}_{y}" for x in range(i, i + 3) for y in range(j, j + 3)])

    # Add initial assignments as constraints
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                problem.addConstraint(lambda value, i=i, j=j: value == board[i][j], (f"cell_{i}_{j}",))

    return problem

def solve_sudoku(board):
    csp = create_sudoku_csp(board)
    solution = csp.getSolution()
    return solution

def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))

def get_user_input():
    print("Enter the Sudoku board:")
    board = []
    for _ in range(9):
        row = list(map(int, input().split()))
        board.append(row)
    return board

if __name__ == "__main__":
    sudoku_board = get_user_input()

    print("\nInitial Sudoku Board:")
    print_sudoku(sudoku_board)

    solution = solve_sudoku(sudoku_board)

    if solution:
        print("\nSolved Sudoku:")
        solved_board = [[solution[f"cell_{i}_{j}"] for j in range(9)] for i in range(9)]
        print_sudoku(solved_board)
    else:
        print("\nNo solution found.")


  .def is_valid_move(board, row, col, num):
    # Check if 'num' is not in the current row, column, and subgrid
    return (
        all(num != board[row][i] for i in range(9)) and
        all(num != board[i][col] for i in range(9)) and
        all(num != board[row // 3 * 3 + i][col // 3 * 3 + j] for i in range(3) for j in range(3))
    )

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)

    if not empty_cell:
        # All cells are filled, the puzzle is solved
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            # If placing 'num' at (row, col) doesn't lead to a solution, backtrack
            board[row][col] = 0

    # No valid number found, backtrack
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

if __name__ == "__main__":
    # Example Sudoku board (0 represents empty cells)
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(sudoku_board):
        print("Sudoku Solution:")
        for row in sudoku_board:
            print(row)
    else:
        print("No solution found.")

user input: def is_valid_move(board, row, col, num):
    return (
        all(num != board[row][i] for i in range(9)) and
        all(num != board[i][col] for i in range(9)) and
        all(num != board[row // 3 * 3 + i][col // 3 * 3 + j] for i in range(3) for j in range(3))
    )

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)

    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def print_board(board):
    for row in board:
        print(" ".join(str(cell) if cell != 0 else '.' for cell in row))

def get_user_input():
    board = []
    print("Enter the Sudoku puzzle row by row. Use '0' for empty cells.")
    for _ in range(9):
        row = input("Enter a row (9 digits separated by space): ").split()
        board.append([int(cell) for cell in row])
    return board

if __name__ == "__main__":
    sudoku_board = get_user_input()

    print("\nInitial Sudoku Puzzle:")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSudoku Solution:")
        print_board(sudoku_board)
    else:
        print("No solution found.")
