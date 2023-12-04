49) Use heuristic search techniques to implement hill climbing algorithm
import random

def objective_function(x):
    # Example objective function (you can replace this with your own function)
    return -((x - 5) ** 2)  # Maximizing a quadratic function

def hill_climbing(initial_solution, max_iterations):
    current_solution = initial_solution

    for _ in range(max_iterations):
        neighbors = generate_neighbors(current_solution)
        neighbor_values = [objective_function(neighbor) for neighbor in neighbors]
        
        best_neighbor = neighbors[neighbor_values.index(max(neighbor_values))]
        
        if objective_function(best_neighbor) > objective_function(current_solution):
            current_solution = best_neighbor

    return current_solution

def generate_neighbors(solution):
    # Simple function to generate neighbors by adding or subtracting a small random value
    return [solution + random.uniform(-0.5, 0.5) for _ in range(5)]

if __name__ == "__main__":
    # Example usage
    initial_solution = random.uniform(0, 10)
    max_iterations = 100

    best_solution = hill_climbing(initial_solution, max_iterations)

    print(f"Best solution found: {best_solution}")
    print(f"Objective function value: {objective_function(best_solution)}")

user input: import random

def objective_function(x):
    # Example objective function (you can replace this with your own function)
    return -((x - 5) ** 2)  # Maximizing a quadratic function

def hill_climbing(initial_solution, max_iterations):
    current_solution = initial_solution

    for _ in range(max_iterations):
        neighbors = generate_neighbors(current_solution)
        neighbor_values = [objective_function(neighbor) for neighbor in neighbors]
        
        best_neighbor = neighbors[neighbor_values.index(max(neighbor_values))]
        
        if objective_function(best_neighbor) > objective_function(current_solution):
            current_solution = best_neighbor

    return current_solution

def generate_neighbors(solution):
    # Simple function to generate neighbors by adding or subtracting a small random value
    return [solution + random.uniform(-0.5, 0.5) for _ in range(5)]

if __name__ == "__main__":
    # User input for initial solution and number of iterations
    initial_solution = float(input("Enter the initial solution: "))
    max_iterations = int(input("Enter the number of iterations: "))

    best_solution = hill_climbing(initial_solution, max_iterations)

    print(f"Best solution found: {best_solution}")
    print(f"Objective function value: {objective_function(best_solution)}")

