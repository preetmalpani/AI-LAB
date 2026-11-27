
import random
import math

N = 8

# Calculate number of attacking queen pairs
def calculate_cost(board):
    cost = 0

    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                cost += 1

    return cost


# Generate neighbouring state
def get_neighbor(board):
    new_board = board.copy()

    col = random.randint(0, N - 1)
    row = random.randint(0, N - 1)

    while row == new_board[col]:
        row = random.randint(0, N - 1)

    new_board[col] = row

    return new_board


# Simulated Annealing Algorithm
def simulated_annealing():

    while True:

        # Random initial configuration
        current = [random.randint(0, N - 1) for _ in range(N)]

        temperature = 100
        cooling_rate = 0.99

        while temperature > 0.1:

            current_cost = calculate_cost(current)

            # Check goal state
            if current_cost == 0:
                return current

            # Generate neighbour
            neighbor = get_neighbor(current)
            neighbor_cost = calculate_cost(neighbor)

            delta = neighbor_cost - current_cost

            # Accept better state
            if delta < 0:
                current = neighbor

            # Accept worse state with probability
            else:
                probability = math.exp(-delta / temperature)

                if random.random() < probability:
                    current = neighbor

            # Cool down
            temperature *= cooling_rate


# Display chessboard
def print_board(board):

    for row in range(N):
        for col in range(N):

            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


# Main program
solution = simulated_annealing()
print("1WA24CS217")
print("Solution:", solution, "| cost =", calculate_cost(solution))

print_board(solution)
