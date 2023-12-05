from queue import PriorityQueue
from collections import deque
from copy import deepcopy
import time

# Define the goal state for the 8-puzzle
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Helper function to find the position of the empty tile
def find_empty_tile(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

# Helper function to calculate the Manhattan distance heuristic
def calculate_manhattan_distance(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                row, col = divmod(board[i][j] - 1, 3)
                distance += abs(i - row) + abs(j - col)
    return distance

# Helper function to check if a board is the goal state
def is_goal_state(board):
    return board == goal_state

# Helper function to get the possible moves from the current board state
def get_possible_moves(board):
    empty_i, empty_j = find_empty_tile(board)
    moves = []

    # Try moving the empty tile in all possible directions
    for move_i, move_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_i, new_j = empty_i + move_i, empty_j + move_j
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_board = deepcopy(board)
            new_board[empty_i][empty_j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[empty_i][empty_j]
            moves.append(new_board)

    return moves

# A* Search Algorithm
def a_star_search(initial_state):
    start_time = time.time()

    open_set = PriorityQueue()
    open_set.put((calculate_manhattan_distance(initial_state), initial_state, []))
    closed_set = set()

    while not open_set.empty():
        _, current_state, path = open_set.get()

        if is_goal_state(current_state):
            end_time = time.time()
            return path, len(path), end_time - start_time

        closed_set.add(tuple(map(tuple, current_state)))

        for move in get_possible_moves(current_state):
            if tuple(map(tuple, move)) not in closed_set:
                new_path = path + [move]
                priority = len(new_path) + calculate_manhattan_distance(move)
                open_set.put((priority, move, new_path))

# Breadth-First Search Algorithm
def breadth_first_search(initial_state):
    start_time = time.time()

    open_set = deque([(initial_state, [])])
    closed_set = set()

    while open_set:
        current_state, path = open_set.popleft()

        if is_goal_state(current_state):
            end_time = time.time()
            return path, len(path), end_time - start_time

        closed_set.add(tuple(map(tuple, current_state)))

        for move in get_possible_moves(current_state):
            if tuple(map(tuple, move)) not in closed_set:
                new_path = path + [move]
                open_set.append((move, new_path))

if __name__ == "__main__":
    # Example initial state
    initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]

    # A* Search
    a_star_path, a_star_steps, a_star_time = a_star_search(initial_state)
    print("A* Search:")
    print("Path:", a_star_path)
    print("Number of steps:", a_star_steps)
    print("Time taken:", a_star_time, "seconds")

    # Breadth-First Search
    bfs_path, bfs_steps, bfs_time = breadth_first_search(initial_state)
    print("\nBreadth-First Search:")
    print("Path:", bfs_path)
    print("Number of steps:", bfs_steps)
    print("Time taken:", bfs_time, "seconds")
