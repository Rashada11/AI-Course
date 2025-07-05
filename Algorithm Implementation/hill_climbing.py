import random

def hill_climb(problem, max_iterations=1000):
    current_solution = problem.initial_solution()  # Start at initial state
    current_value = problem.evaluate(current_solution)  # Evaluate initial state

    for _ in range(max_iterations):  
        neighbors = problem.generate_neighbors(current_solution)  # Get neighboring solutions
        best_neighbor = max(neighbors, key=problem.evaluate)  # Select the best neighbor

        if problem.evaluate(best_neighbor) <= current_value:  # Stop if no improvement
            break

        current_solution = best_neighbor  # Move to better neighbor
        current_value = problem.evaluate(current_solution)  # Update value

    return current_solution

# Example Problem: Maximize f(x) = -x^2 + 4x in range [0, 4]
class ExampleProblem:
    def initial_solution(self):
        return random.uniform(0, 4)  # Random start in the range [0,4]

    def evaluate(self, x):
        return -x**2 + 4*x  # Function to maximize

    def generate_neighbors(self, x):
        step = 0.1  # Small adjustment to explore new solutions
        return [x + step, x - step]  # Two nearby values

problem = ExampleProblem()
best_solution = hill_climb(problem)
print(f"Best Found Solution: x = {best_solution}, f(x) = {problem.evaluate(best_solution)}")
