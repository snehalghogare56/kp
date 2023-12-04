def is_safe(board, row, col, n):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    if col == n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1, n):
                return True
            board[i][col] = 0

    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist.")
        return

    print_solution(board)

def print_solution(board):
    for row in board:
        print(" ".join(["Q" if col == 1 else "." for col in row]))

if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    solve_n_queens(n)
csp:
pip install python-constraint
 from constraint import Problem, AllDifferentConstraint

def n_queens(n):
    problem = Problem()
    
    # Define variables (queen positions)
    problem.addVariables(range(n), range(n))
    
    # Add constraints
    problem.addConstraint(AllDifferentConstraint())
    
    def diagonal_constraint(q1, q2, d):
        return abs(q1 - q2) != d
    
    for i in range(n):
        for j in range(i + 1, n):
            problem.addConstraint(diagonal_constraint, (i, j, j - i))
            problem.addConstraint(diagonal_constraint, (i, j, i - j))
    
    # Find solution
    solutions = problem.getSolutions()
    
    return solutions

def print_solution(solution):
    for row in solution:
        line = ["Q" if col == row else "." for col in solution[row]]
        print(" ".join(line))

if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    
    solutions = n_queens(n)
    
    print(f"\nTotal solutions found: {len(solutions)}")
    if solutions:
        print("\nOne of the solutions:")
        print_solution(solutions[0])
