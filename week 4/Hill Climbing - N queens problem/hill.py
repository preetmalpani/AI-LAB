
N = 4

# Calculate cost (number of attacking queen pairs)
def calculate_cost(board):
    cost = 0

    for i in range(N):
        for j in range(i + 1, N):

            # Check same row or diagonal
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                cost += 1

    return cost


# Generate neighbouring states
def get_neighbors(board):
    neighbors = []

    for col in range(N):
        for row in range(N):

            if row != board[col]:
                new_board = board.copy()
                new_board[col] = row
                neighbors.append(new_board)

    return neighbors


# Display chessboard
def print_board(board):
    print("\nQueen Representation:")

    for row in range(N):
        for col in range(N):

            if board[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")

        print()


# Hill Climbing Algorithm
def hill_climbing():
    print("1WA24CS217")
    # Take initial configuration from user
    board = list(map(int, input(
        "Enter initial configuration (4 values between 0 and 3): "
    ).split()))

    if len(board) != N or any(x < 0 or x >= N for x in board):
        print("Invalid input! Enter exactly 4 values between 0 and 3.")
        return

    step = 1

    while True:

        current_cost = calculate_cost(board)

        print("\n-----------------------------")
        print("Step:", step)
        print("Current State:", board)
        print("Current Cost:", current_cost)

        print_board(board)

        # Check goal state
        if current_cost == 0:
            print("\nGOAL STATE REACHED!")
            print("Final Configuration:", board)
            print("Final Cost:", current_cost)
            break

        # Generate neighbours
        neighbors = get_neighbors(board)

        print("\nNeighbour States and Costs:")

        for neighbor in neighbors:
            print(neighbor, "-> Cost:", calculate_cost(neighbor))

        # Select neighbour with minimum cost
        best_neighbor = min(neighbors, key=calculate_cost)
        best_cost = calculate_cost(best_neighbor)

        print("\nBest Neighbour:", best_neighbor)
        print("Best Neighbour Cost:", best_cost)

        # Check for local minimum
        if best_cost >= current_cost:
            print("\nLOCAL MINIMUM REACHED!")
            print("No better neighbour found.")
            print("Try another initial configuration.")
            break

        # Move to best neighbour
        board = best_neighbor
        step += 1


# Main program
hill_climbing()
