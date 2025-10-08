import random
import math

def cost(state):
    attacking_pairs = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacking_pairs += 1
    return attacking_pairs

def print_board(state):
    n = len(state)
    board = [['.' for _ in range(n)] for _ in range(n)]
    for col in range(n):
        row = state[col]
        board[row][col] = 'Q'
    for row in board:
        print(" ".join(row))
    print()

def get_neighbors(state):
    neighbors = []
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            neighbor = list(state)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(tuple(neighbor))
    return neighbors

def simulated_annealing(initial_state, initial_temp=100, cooling_rate=0.99, min_temp=0.1):
    current = initial_state
    best = current
    T = initial_temp
    print("Initial State:")
    print_board(current)
    print(f"Initial Cost: {cost(current)}")
    print('-' * 30)
    while T > min_temp:
        neighbors = get_neighbors(current)
        next_state = random.choice(neighbors)
        delta_E = cost(next_state) - cost(current)
        if delta_E < 0 or random.random() < math.exp(-delta_E / T):
            current = next_state
        if cost(current) < cost(best):
            best = current
        T = T * cooling_rate
        print(f"Temperature: {T:.2f} | Cost: {cost(current)} | Best: {cost(best)}")
    print('-' * 30)
    print("Final Solution Found:")
    print_board(best)
    print(f"Final Cost: {cost(best)}")
    return best

if __name__ == "__main__":
    n = 5
    initial_state = tuple(random.sample(range(n), n))
    solution = simulated_annealing(initial_state)


# OUTPUT:
# Initial State:
# Q . . . .
# . . . Q .
# . . . . Q
# . Q . . .
# . . Q . .

# Initial Cost: 4
# ------------------------------
# Temperature: 99.00 | Cost: 0 | Best: 0
# Temperature: 98.01 | Cost: 2 | Best: 0
# Temperature: 97.03 | Cost: 4 | Best: 0
# Temperature: 96.06 | Cost: 6 | Best: 0
# Temperature: 95.10 | Cost: 2 | Best: 0
# Temperature: 94.15 | Cost: 6 | Best: 0
# Temperature: 93.21 | Cost: 4 | Best: 0
# Temperature: 92.27 | Cost: 2 | Best: 0
# Temperature: 91.35 | Cost: 4 | Best: 0
# Temperature: 90.44 | Cost: 2 | Best: 0
# Temperature: 89.53 | Cost: 4 | Best: 0
# Temperature: 88.64 | Cost: 2 | Best: 0
# Temperature: 87.75 | Cost: 2 | Best: 0
# Temperature: 86.87 | Cost: 2 | Best: 0
# Temperature: 86.01 | Cost: 2 | Best: 0
# Temperature: 85.15 | Cost: 2 | Best: 0
# Temperature: 84.29 | Cost: 4 | Best: 0
# Temperature: 83.45 | Cost: 4 | Best: 0
# Temperature: 82.62 | Cost: 4 | Best: 0
# Temperature: 81.79 | Cost: 2 | Best: 0
# Temperature: 80.97 | Cost: 4 | Best: 0
# Temperature: 80.16 | Cost: 4 | Best: 0
# Temperature: 79.36 | Cost: 0 | Best: 0
# Temperature: 78.57 | Cost: 4 | Best: 0
# Temperature: 77.78 | Cost: 2 | Best: 0
# Temperature: 77.00 | Cost: 2 | Best: 0
# Temperature: 76.23 | Cost: 2 | Best: 0
# Temperature: 75.47 | Cost: 2 | Best: 0
# Temperature: 74.72 | Cost: 0 | Best: 0
# Temperature: 73.97 | Cost: 2 | Best: 0
# Temperature: 73.23 | Cost: 4 | Best: 0
# Temperature: 72.50 | Cost: 2 | Best: 0
# Temperature: 71.77 | Cost: 2 | Best: 0
# Temperature: 71.06 | Cost: 2 | Best: 0
# Temperature: 70.34 | Cost: 2 | Best: 0
# Temperature: 69.64 | Cost: 2 | Best: 0
# Temperature: 68.94 | Cost: 0 | Best: 0
# Temperature: 68.26 | Cost: 4 | Best: 0
# Temperature: 67.57 | Cost: 4 | Best: 0
# Temperature: 66.90 | Cost: 2 | Best: 0
# Temperature: 66.23 | Cost: 2 | Best: 0
# Temperature: 65.57 | Cost: 2 | Best: 0
# Temperature: 64.91 | Cost: 0 | Best: 0
# Temperature: 64.26 | Cost: 2 | Best: 0
# Temperature: 63.62 | Cost: 6 | Best: 0
# Temperature: 62.98 | Cost: 2 | Best: 0
# Temperature: 62.35 | Cost: 4 | Best: 0
# Temperature: 61.73 | Cost: 2 | Best: 0
# Temperature: 61.11 | Cost: 4 | Best: 0
# Temperature: 60.50 | Cost: 2 | Best: 0
# Temperature: 59.90 | Cost: 0 | Best: 0
# Temperature: 59.30 | Cost: 2 | Best: 0
# Temperature: 58.70 | Cost: 0 | Best: 0
# Temperature: 58.12 | Cost: 2 | Best: 0
# Temperature: 57.54 | Cost: 4 | Best: 0
# Temperature: 56.96 | Cost: 4 | Best: 0
# Temperature: 56.39 | Cost: 10 | Best: 0
# Temperature: 55.83 | Cost: 6 | Best: 0
# Temperature: 55.27 | Cost: 4 | Best: 0
# Temperature: 54.72 | Cost: 6 | Best: 0
# Temperature: 54.17 | Cost: 4 | Best: 0
# Temperature: 53.63 | Cost: 6 | Best: 0
# Temperature: 53.09 | Cost: 4 | Best: 0
# Temperature: 52.56 | Cost: 0 | Best: 0
# Temperature: 52.03 | Cost: 2 | Best: 0
# Temperature: 51.51 | Cost: 4 | Best: 0
# Temperature: 51.00 | Cost: 2 | Best: 0
# Temperature: 50.49 | Cost: 2 | Best: 0
# Temperature: 49.98 | Cost: 2 | Best: 0
# Temperature: 49.48 | Cost: 4 | Best: 0
# Temperature: 48.99 | Cost: 2 | Best: 0
# Temperature: 48.50 | Cost: 4 | Best: 0
# Temperature: 48.01 | Cost: 2 | Best: 0
# Temperature: 47.53 | Cost: 4 | Best: 0
# Temperature: 47.06 | Cost: 2 | Best: 0
# Temperature: 46.59 | Cost: 0 | Best: 0
# Temperature: 46.12 | Cost: 0 | Best: 0
# Temperature: 45.66 | Cost: 0 | Best: 0
# Temperature: 45.20 | Cost: 2 | Best: 0
# Temperature: 44.75 | Cost: 4 | Best: 0
# Temperature: 44.30 | Cost: 2 | Best: 0
# Temperature: 43.86 | Cost: 4 | Best: 0
# Temperature: 43.42 | Cost: 2 | Best: 0
# Temperature: 42.99 | Cost: 4 | Best: 0
# Temperature: 42.56 | Cost: 2 | Best: 0
# Temperature: 42.13 | Cost: 4 | Best: 0
# Temperature: 41.71 | Cost: 2 | Best: 0
# Temperature: 41.29 | Cost: 4 | Best: 0
# Temperature: 40.88 | Cost: 4 | Best: 0
# Temperature: 40.47 | Cost: 4 | Best: 0
# Temperature: 40.07 | Cost: 2 | Best: 0
# Temperature: 39.67 | Cost: 2 | Best: 0
# Temperature: 39.27 | Cost: 2 | Best: 0
# Temperature: 38.88 | Cost: 6 | Best: 0
# Temperature: 38.49 | Cost: 2 | Best: 0
# Temperature: 38.10 | Cost: 2 | Best: 0
# Temperature: 37.72 | Cost: 2 | Best: 0
# Temperature: 37.35 | Cost: 4 | Best: 0
# Temperature: 36.97 | Cost: 6 | Best: 0
# Temperature: 36.60 | Cost: 4 | Best: 0
# Temperature: 36.24 | Cost: 4 | Best: 0
# Temperature: 35.87 | Cost: 4 | Best: 0
# Temperature: 35.52 | Cost: 4 | Best: 0
# Temperature: 35.16 | Cost: 0 | Best: 0
# Temperature: 34.81 | Cost: 2 | Best: 0
# Temperature: 34.46 | Cost: 4 | Best: 0
# Temperature: 34.12 | Cost: 2 | Best: 0
# Temperature: 33.78 | Cost: 4 | Best: 0
# Temperature: 33.44 | Cost: 6 | Best: 0
# Temperature: 33.10 | Cost: 2 | Best: 0
# Temperature: 32.77 | Cost: 2 | Best: 0
# Temperature: 32.44 | Cost: 4 | Best: 0
# Temperature: 32.12 | Cost: 2 | Best: 0
# Temperature: 31.80 | Cost: 2 | Best: 0
# Temperature: 31.48 | Cost: 4 | Best: 0
# Temperature: 31.17 | Cost: 6 | Best: 0
# Temperature: 30.85 | Cost: 4 | Best: 0
# Temperature: 30.55 | Cost: 2 | Best: 0
# Temperature: 30.24 | Cost: 2 | Best: 0
# Temperature: 29.94 | Cost: 4 | Best: 0
# Temperature: 29.64 | Cost: 2 | Best: 0
# Temperature: 29.34 | Cost: 0 | Best: 0
# Temperature: 29.05 | Cost: 2 | Best: 0
# Temperature: 28.76 | Cost: 2 | Best: 0
# Temperature: 28.47 | Cost: 2 | Best: 0
# Temperature: 28.19 | Cost: 0 | Best: 0
# Temperature: 27.90 | Cost: 2 | Best: 0
# Temperature: 27.63 | Cost: 4 | Best: 0
# Temperature: 27.35 | Cost: 6 | Best: 0
# Temperature: 27.08 | Cost: 2 | Best: 0
# Temperature: 26.80 | Cost: 2 | Best: 0
# Temperature: 26.54 | Cost: 0 | Best: 0
# Temperature: 26.27 | Cost: 2 | Best: 0
# Temperature: 26.01 | Cost: 4 | Best: 0
# Temperature: 25.75 | Cost: 2 | Best: 0
# Temperature: 25.49 | Cost: 2 | Best: 0
# Temperature: 25.24 | Cost: 2 | Best: 0
# Temperature: 24.98 | Cost: 6 | Best: 0
# Temperature: 24.73 | Cost: 2 | Best: 0
# Temperature: 24.49 | Cost: 4 | Best: 0
# Temperature: 24.24 | Cost: 4 | Best: 0
# Temperature: 24.00 | Cost: 4 | Best: 0
# Temperature: 23.76 | Cost: 2 | Best: 0
# Temperature: 23.52 | Cost: 2 | Best: 0
# Temperature: 23.29 | Cost: 2 | Best: 0
# Temperature: 23.05 | Cost: 0 | Best: 0
# Temperature: 22.82 | Cost: 2 | Best: 0
# Temperature: 22.59 | Cost: 2 | Best: 0
# Temperature: 22.37 | Cost: 2 | Best: 0
# Temperature: 22.15 | Cost: 2 | Best: 0
# Temperature: 21.92 | Cost: 2 | Best: 0
# Temperature: 21.70 | Cost: 6 | Best: 0
# Temperature: 21.49 | Cost: 2 | Best: 0
# Temperature: 21.27 | Cost: 2 | Best: 0
# Temperature: 21.06 | Cost: 2 | Best: 0
# Temperature: 20.85 | Cost: 6 | Best: 0
# Temperature: 20.64 | Cost: 4 | Best: 0
# Temperature: 20.43 | Cost: 2 | Best: 0
# Temperature: 20.23 | Cost: 2 | Best: 0
# Temperature: 20.03 | Cost: 2 | Best: 0
# Temperature: 19.83 | Cost: 6 | Best: 0
# Temperature: 19.63 | Cost: 2 | Best: 0
# Temperature: 19.43 | Cost: 4 | Best: 0
# Temperature: 19.24 | Cost: 4 | Best: 0
# Temperature: 19.05 | Cost: 0 | Best: 0
# Temperature: 18.86 | Cost: 2 | Best: 0
# Temperature: 18.67 | Cost: 4 | Best: 0
# Temperature: 18.48 | Cost: 4 | Best: 0
# Temperature: 18.30 | Cost: 2 | Best: 0
# Temperature: 18.11 | Cost: 2 | Best: 0
# Temperature: 17.93 | Cost: 6 | Best: 0
# Temperature: 17.75 | Cost: 4 | Best: 0
# Temperature: 17.57 | Cost: 2 | Best: 0
# Temperature: 17.40 | Cost: 0 | Best: 0
# Temperature: 17.22 | Cost: 2 | Best: 0
# Temperature: 17.05 | Cost: 4 | Best: 0
# Temperature: 16.88 | Cost: 4 | Best: 0
# Temperature: 16.71 | Cost: 4 | Best: 0
# Temperature: 16.55 | Cost: 2 | Best: 0
# Temperature: 16.38 | Cost: 4 | Best: 0
# Temperature: 16.22 | Cost: 6 | Best: 0
# Temperature: 16.05 | Cost: 4 | Best: 0
# Temperature: 15.89 | Cost: 2 | Best: 0
# Temperature: 15.74 | Cost: 4 | Best: 0
# Temperature: 15.58 | Cost: 4 | Best: 0
# Temperature: 15.42 | Cost: 4 | Best: 0
# Temperature: 15.27 | Cost: 2 | Best: 0
# Temperature: 15.12 | Cost: 2 | Best: 0
# Temperature: 14.96 | Cost: 4 | Best: 0
# Temperature: 14.81 | Cost: 2 | Best: 0
# Temperature: 14.67 | Cost: 4 | Best: 0
# Temperature: 14.52 | Cost: 4 | Best: 0
# Temperature: 14.37 | Cost: 6 | Best: 0
# Temperature: 14.23 | Cost: 4 | Best: 0
# Temperature: 14.09 | Cost: 2 | Best: 0
# Temperature: 13.95 | Cost: 4 | Best: 0
# Temperature: 13.81 | Cost: 4 | Best: 0
# Temperature: 13.67 | Cost: 4 | Best: 0
# Temperature: 13.53 | Cost: 6 | Best: 0
# Temperature: 13.40 | Cost: 4 | Best: 0
# Temperature: 13.26 | Cost: 4 | Best: 0
# Temperature: 13.13 | Cost: 4 | Best: 0
# Temperature: 13.00 | Cost: 2 | Best: 0
# Temperature: 12.87 | Cost: 6 | Best: 0
# Temperature: 12.74 | Cost: 4 | Best: 0
# Temperature: 12.61 | Cost: 2 | Best: 0
# Temperature: 12.49 | Cost: 4 | Best: 0
# Temperature: 12.36 | Cost: 2 | Best: 0
# Temperature: 12.24 | Cost: 2 | Best: 0
# Temperature: 12.12 | Cost: 0 | Best: 0
# Temperature: 12.00 | Cost: 2 | Best: 0
# Temperature: 11.88 | Cost: 4 | Best: 0
# Temperature: 11.76 | Cost: 2 | Best: 0
# Temperature: 11.64 | Cost: 2 | Best: 0
# Temperature: 11.52 | Cost: 4 | Best: 0
# Temperature: 11.41 | Cost: 2 | Best: 0
# Temperature: 11.29 | Cost: 4 | Best: 0
# Temperature: 11.18 | Cost: 6 | Best: 0
# Temperature: 11.07 | Cost: 10 | Best: 0
# Temperature: 10.96 | Cost: 4 | Best: 0
# Temperature: 10.85 | Cost: 6 | Best: 0
# Temperature: 10.74 | Cost: 4 | Best: 0
# Temperature: 10.63 | Cost: 2 | Best: 0
# Temperature: 10.53 | Cost: 4 | Best: 0
# Temperature: 10.42 | Cost: 2 | Best: 0
# Temperature: 10.32 | Cost: 4 | Best: 0
# Temperature: 10.21 | Cost: 10 | Best: 0
# Temperature: 10.11 | Cost: 4 | Best: 0
# Temperature: 10.01 | Cost: 2 | Best: 0
# Temperature: 9.91 | Cost: 2 | Best: 0
# Temperature: 9.81 | Cost: 2 | Best: 0
# Temperature: 9.71 | Cost: 2 | Best: 0
# Temperature: 9.62 | Cost: 4 | Best: 0
# Temperature: 9.52 | Cost: 10 | Best: 0
# Temperature: 9.42 | Cost: 4 | Best: 0
# Temperature: 9.33 | Cost: 2 | Best: 0
# Temperature: 9.24 | Cost: 4 | Best: 0
# Temperature: 9.14 | Cost: 2 | Best: 0
# Temperature: 9.05 | Cost: 2 | Best: 0
# Temperature: 8.96 | Cost: 4 | Best: 0
# Temperature: 8.87 | Cost: 6 | Best: 0
# Temperature: 8.78 | Cost: 4 | Best: 0
# Temperature: 8.70 | Cost: 2 | Best: 0
# Temperature: 8.61 | Cost: 6 | Best: 0
# Temperature: 8.52 | Cost: 6 | Best: 0
# Temperature: 8.44 | Cost: 2 | Best: 0
# Temperature: 8.35 | Cost: 0 | Best: 0
# Temperature: 8.27 | Cost: 4 | Best: 0
# Temperature: 8.19 | Cost: 4 | Best: 0
# Temperature: 8.11 | Cost: 4 | Best: 0
# Temperature: 8.02 | Cost: 4 | Best: 0
# Temperature: 7.94 | Cost: 4 | Best: 0
# Temperature: 7.87 | Cost: 4 | Best: 0
# Temperature: 7.79 | Cost: 2 | Best: 0
# Temperature: 7.71 | Cost: 2 | Best: 0
# Temperature: 7.63 | Cost: 6 | Best: 0
# Temperature: 7.56 | Cost: 2 | Best: 0
# Temperature: 7.48 | Cost: 0 | Best: 0
# Temperature: 7.40 | Cost: 2 | Best: 0
# Temperature: 7.33 | Cost: 4 | Best: 0
# Temperature: 7.26 | Cost: 2 | Best: 0
# Temperature: 7.18 | Cost: 0 | Best: 0
# Temperature: 7.11 | Cost: 2 | Best: 0
# Temperature: 7.04 | Cost: 4 | Best: 0
# Temperature: 6.97 | Cost: 2 | Best: 0
# Temperature: 6.90 | Cost: 2 | Best: 0
# Temperature: 6.83 | Cost: 2 | Best: 0
# Temperature: 6.76 | Cost: 2 | Best: 0
# Temperature: 6.70 | Cost: 2 | Best: 0
# Temperature: 6.63 | Cost: 2 | Best: 0
# Temperature: 6.56 | Cost: 2 | Best: 0
# Temperature: 6.50 | Cost: 0 | Best: 0
# Temperature: 6.43 | Cost: 4 | Best: 0
# Temperature: 6.37 | Cost: 2 | Best: 0
# Temperature: 6.30 | Cost: 2 | Best: 0
# Temperature: 6.24 | Cost: 4 | Best: 0
# Temperature: 6.18 | Cost: 2 | Best: 0
# Temperature: 6.12 | Cost: 4 | Best: 0
# Temperature: 6.06 | Cost: 10 | Best: 0
# Temperature: 6.00 | Cost: 4 | Best: 0
# Temperature: 5.94 | Cost: 2 | Best: 0
# Temperature: 5.88 | Cost: 2 | Best: 0
# Temperature: 5.82 | Cost: 4 | Best: 0
# Temperature: 5.76 | Cost: 2 | Best: 0
# Temperature: 5.70 | Cost: 2 | Best: 0
# Temperature: 5.65 | Cost: 2 | Best: 0
# Temperature: 5.59 | Cost: 2 | Best: 0
# Temperature: 5.53 | Cost: 2 | Best: 0
# Temperature: 5.48 | Cost: 4 | Best: 0
# Temperature: 5.42 | Cost: 4 | Best: 0
# Temperature: 5.37 | Cost: 4 | Best: 0
# Temperature: 5.31 | Cost: 4 | Best: 0
# Temperature: 5.26 | Cost: 4 | Best: 0
# Temperature: 5.21 | Cost: 4 | Best: 0
# Temperature: 5.16 | Cost: 4 | Best: 0
# Temperature: 5.11 | Cost: 4 | Best: 0
# Temperature: 5.05 | Cost: 2 | Best: 0
# Temperature: 5.00 | Cost: 0 | Best: 0
# Temperature: 4.95 | Cost: 0 | Best: 0
# Temperature: 4.90 | Cost: 2 | Best: 0
# Temperature: 4.86 | Cost: 4 | Best: 0
# Temperature: 4.81 | Cost: 2 | Best: 0
# Temperature: 4.76 | Cost: 4 | Best: 0
# Temperature: 4.71 | Cost: 4 | Best: 0
# Temperature: 4.66 | Cost: 2 | Best: 0
# Temperature: 4.62 | Cost: 2 | Best: 0
# Temperature: 4.57 | Cost: 2 | Best: 0
# Temperature: 4.53 | Cost: 4 | Best: 0
# Temperature: 4.48 | Cost: 4 | Best: 0
# Temperature: 4.44 | Cost: 2 | Best: 0
# Temperature: 4.39 | Cost: 0 | Best: 0
# Temperature: 4.35 | Cost: 2 | Best: 0
# Temperature: 4.30 | Cost: 0 | Best: 0
# Temperature: 4.26 | Cost: 2 | Best: 0
# Temperature: 4.22 | Cost: 2 | Best: 0
# Temperature: 4.18 | Cost: 6 | Best: 0
# Temperature: 4.13 | Cost: 4 | Best: 0
# Temperature: 4.09 | Cost: 6 | Best: 0
# Temperature: 4.05 | Cost: 4 | Best: 0
# Temperature: 4.01 | Cost: 2 | Best: 0
# Temperature: 3.97 | Cost: 2 | Best: 0
# Temperature: 3.93 | Cost: 4 | Best: 0
# Temperature: 3.89 | Cost: 4 | Best: 0
# Temperature: 3.85 | Cost: 4 | Best: 0
# Temperature: 3.81 | Cost: 4 | Best: 0
# Temperature: 3.78 | Cost: 2 | Best: 0
# Temperature: 3.74 | Cost: 2 | Best: 0
# Temperature: 3.70 | Cost: 2 | Best: 0
# Temperature: 3.66 | Cost: 0 | Best: 0
# Temperature: 3.63 | Cost: 2 | Best: 0
# Temperature: 3.59 | Cost: 0 | Best: 0
# Temperature: 3.56 | Cost: 0 | Best: 0
# Temperature: 3.52 | Cost: 2 | Best: 0
# Temperature: 3.48 | Cost: 2 | Best: 0
# Temperature: 3.45 | Cost: 4 | Best: 0
# Temperature: 3.42 | Cost: 0 | Best: 0
# Temperature: 3.38 | Cost: 0 | Best: 0
# Temperature: 3.35 | Cost: 0 | Best: 0
# Temperature: 3.31 | Cost: 2 | Best: 0
# Temperature: 3.28 | Cost: 0 | Best: 0
# Temperature: 3.25 | Cost: 2 | Best: 0
# Temperature: 3.22 | Cost: 4 | Best: 0
# Temperature: 3.18 | Cost: 4 | Best: 0
# Temperature: 3.15 | Cost: 4 | Best: 0
# Temperature: 3.12 | Cost: 4 | Best: 0
# Temperature: 3.09 | Cost: 2 | Best: 0
# Temperature: 3.06 | Cost: 2 | Best: 0
# Temperature: 3.03 | Cost: 4 | Best: 0
# Temperature: 3.00 | Cost: 4 | Best: 0
# Temperature: 2.97 | Cost: 0 | Best: 0
# Temperature: 2.94 | Cost: 0 | Best: 0
# Temperature: 2.91 | Cost: 0 | Best: 0
# Temperature: 2.88 | Cost: 2 | Best: 0
# Temperature: 2.85 | Cost: 6 | Best: 0
# Temperature: 2.82 | Cost: 2 | Best: 0
# Temperature: 2.79 | Cost: 4 | Best: 0
# Temperature: 2.77 | Cost: 2 | Best: 0
# Temperature: 2.74 | Cost: 2 | Best: 0
# Temperature: 2.71 | Cost: 2 | Best: 0
# Temperature: 2.68 | Cost: 0 | Best: 0
# Temperature: 2.66 | Cost: 2 | Best: 0
# Temperature: 2.63 | Cost: 0 | Best: 0
# Temperature: 2.60 | Cost: 0 | Best: 0
# Temperature: 2.58 | Cost: 0 | Best: 0
# Temperature: 2.55 | Cost: 0 | Best: 0
# Temperature: 2.53 | Cost: 0 | Best: 0
# Temperature: 2.50 | Cost: 2 | Best: 0
# Temperature: 2.48 | Cost: 4 | Best: 0
# Temperature: 2.45 | Cost: 2 | Best: 0
# Temperature: 2.43 | Cost: 2 | Best: 0
# Temperature: 2.40 | Cost: 2 | Best: 0
# Temperature: 2.38 | Cost: 2 | Best: 0
# Temperature: 2.35 | Cost: 2 | Best: 0
# Temperature: 2.33 | Cost: 2 | Best: 0
# Temperature: 2.31 | Cost: 2 | Best: 0
# Temperature: 2.28 | Cost: 2 | Best: 0
# Temperature: 2.26 | Cost: 2 | Best: 0
# Temperature: 2.24 | Cost: 2 | Best: 0
# Temperature: 2.22 | Cost: 2 | Best: 0
# Temperature: 2.19 | Cost: 2 | Best: 0
# Temperature: 2.17 | Cost: 2 | Best: 0
# Temperature: 2.15 | Cost: 2 | Best: 0
# Temperature: 2.13 | Cost: 2 | Best: 0
# Temperature: 2.11 | Cost: 2 | Best: 0
# Temperature: 2.09 | Cost: 4 | Best: 0
# Temperature: 2.07 | Cost: 4 | Best: 0
# Temperature: 2.05 | Cost: 2 | Best: 0
# Temperature: 2.03 | Cost: 2 | Best: 0
# Temperature: 2.00 | Cost: 6 | Best: 0
# Temperature: 1.98 | Cost: 6 | Best: 0
# Temperature: 1.96 | Cost: 2 | Best: 0
# Temperature: 1.95 | Cost: 4 | Best: 0
# Temperature: 1.93 | Cost: 2 | Best: 0
# Temperature: 1.91 | Cost: 2 | Best: 0
# Temperature: 1.89 | Cost: 4 | Best: 0
# Temperature: 1.87 | Cost: 4 | Best: 0
# Temperature: 1.85 | Cost: 2 | Best: 0
# Temperature: 1.83 | Cost: 4 | Best: 0
# Temperature: 1.81 | Cost: 4 | Best: 0
# Temperature: 1.80 | Cost: 2 | Best: 0
# Temperature: 1.78 | Cost: 2 | Best: 0
# Temperature: 1.76 | Cost: 2 | Best: 0
# Temperature: 1.74 | Cost: 2 | Best: 0
# Temperature: 1.72 | Cost: 2 | Best: 0
# Temperature: 1.71 | Cost: 2 | Best: 0
# Temperature: 1.69 | Cost: 2 | Best: 0
# Temperature: 1.67 | Cost: 2 | Best: 0
# Temperature: 1.66 | Cost: 2 | Best: 0
# Temperature: 1.64 | Cost: 4 | Best: 0
# Temperature: 1.62 | Cost: 2 | Best: 0
# Temperature: 1.61 | Cost: 2 | Best: 0
# Temperature: 1.59 | Cost: 2 | Best: 0
# Temperature: 1.58 | Cost: 2 | Best: 0
# Temperature: 1.56 | Cost: 2 | Best: 0
# Temperature: 1.54 | Cost: 2 | Best: 0
# Temperature: 1.53 | Cost: 0 | Best: 0
# Temperature: 1.51 | Cost: 0 | Best: 0
# Temperature: 1.50 | Cost: 0 | Best: 0
# Temperature: 1.48 | Cost: 2 | Best: 0
# Temperature: 1.47 | Cost: 2 | Best: 0
# Temperature: 1.45 | Cost: 2 | Best: 0
# Temperature: 1.44 | Cost: 2 | Best: 0
# Temperature: 1.42 | Cost: 2 | Best: 0
# Temperature: 1.41 | Cost: 2 | Best: 0
# Temperature: 1.40 | Cost: 2 | Best: 0
# Temperature: 1.38 | Cost: 2 | Best: 0
# Temperature: 1.37 | Cost: 2 | Best: 0
# Temperature: 1.35 | Cost: 2 | Best: 0
# Temperature: 1.34 | Cost: 2 | Best: 0
# Temperature: 1.33 | Cost: 4 | Best: 0
# Temperature: 1.31 | Cost: 4 | Best: 0
# Temperature: 1.30 | Cost: 2 | Best: 0
# Temperature: 1.29 | Cost: 0 | Best: 0
# Temperature: 1.28 | Cost: 0 | Best: 0
# Temperature: 1.26 | Cost: 0 | Best: 0
# Temperature: 1.25 | Cost: 0 | Best: 0
# Temperature: 1.24 | Cost: 0 | Best: 0
# Temperature: 1.23 | Cost: 0 | Best: 0
# Temperature: 1.21 | Cost: 2 | Best: 0
# Temperature: 1.20 | Cost: 2 | Best: 0
# Temperature: 1.19 | Cost: 2 | Best: 0
# Temperature: 1.18 | Cost: 0 | Best: 0
# Temperature: 1.17 | Cost: 2 | Best: 0
# Temperature: 1.15 | Cost: 2 | Best: 0
# Temperature: 1.14 | Cost: 4 | Best: 0
# Temperature: 1.13 | Cost: 2 | Best: 0
# Temperature: 1.12 | Cost: 4 | Best: 0
# Temperature: 1.11 | Cost: 2 | Best: 0
# Temperature: 1.10 | Cost: 0 | Best: 0
# Temperature: 1.09 | Cost: 0 | Best: 0
# Temperature: 1.08 | Cost: 2 | Best: 0
# Temperature: 1.06 | Cost: 2 | Best: 0
# Temperature: 1.05 | Cost: 2 | Best: 0
# Temperature: 1.04 | Cost: 2 | Best: 0
# Temperature: 1.03 | Cost: 2 | Best: 0
# Temperature: 1.02 | Cost: 2 | Best: 0
# Temperature: 1.01 | Cost: 0 | Best: 0
# Temperature: 1.00 | Cost: 0 | Best: 0
# Temperature: 0.99 | Cost: 0 | Best: 0
# Temperature: 0.98 | Cost: 0 | Best: 0
# Temperature: 0.97 | Cost: 0 | Best: 0
# Temperature: 0.96 | Cost: 2 | Best: 0
# Temperature: 0.95 | Cost: 2 | Best: 0
# Temperature: 0.94 | Cost: 2 | Best: 0
# Temperature: 0.93 | Cost: 2 | Best: 0
# Temperature: 0.92 | Cost: 2 | Best: 0
# Temperature: 0.92 | Cost: 2 | Best: 0
# Temperature: 0.91 | Cost: 2 | Best: 0
# Temperature: 0.90 | Cost: 2 | Best: 0
# Temperature: 0.89 | Cost: 2 | Best: 0
# Temperature: 0.88 | Cost: 2 | Best: 0
# Temperature: 0.87 | Cost: 2 | Best: 0
# Temperature: 0.86 | Cost: 2 | Best: 0
# Temperature: 0.85 | Cost: 2 | Best: 0
# Temperature: 0.84 | Cost: 0 | Best: 0
# Temperature: 0.84 | Cost: 0 | Best: 0
# Temperature: 0.83 | Cost: 0 | Best: 0
# Temperature: 0.82 | Cost: 0 | Best: 0
# Temperature: 0.81 | Cost: 0 | Best: 0
# Temperature: 0.80 | Cost: 0 | Best: 0
# Temperature: 0.80 | Cost: 0 | Best: 0
# Temperature: 0.79 | Cost: 0 | Best: 0
# Temperature: 0.78 | Cost: 0 | Best: 0
# Temperature: 0.77 | Cost: 0 | Best: 0
# Temperature: 0.76 | Cost: 0 | Best: 0
# Temperature: 0.76 | Cost: 0 | Best: 0
# Temperature: 0.75 | Cost: 0 | Best: 0
# Temperature: 0.74 | Cost: 0 | Best: 0
# Temperature: 0.73 | Cost: 0 | Best: 0
# Temperature: 0.73 | Cost: 0 | Best: 0
# Temperature: 0.72 | Cost: 0 | Best: 0
# Temperature: 0.71 | Cost: 0 | Best: 0
# Temperature: 0.70 | Cost: 0 | Best: 0
# Temperature: 0.70 | Cost: 0 | Best: 0
# Temperature: 0.69 | Cost: 0 | Best: 0
# Temperature: 0.68 | Cost: 0 | Best: 0
# Temperature: 0.68 | Cost: 0 | Best: 0
# Temperature: 0.67 | Cost: 0 | Best: 0
# Temperature: 0.66 | Cost: 0 | Best: 0
# Temperature: 0.66 | Cost: 0 | Best: 0
# Temperature: 0.65 | Cost: 0 | Best: 0
# Temperature: 0.64 | Cost: 0 | Best: 0
# Temperature: 0.64 | Cost: 0 | Best: 0
# Temperature: 0.63 | Cost: 0 | Best: 0
# Temperature: 0.62 | Cost: 0 | Best: 0
# Temperature: 0.62 | Cost: 0 | Best: 0
# Temperature: 0.61 | Cost: 0 | Best: 0
# Temperature: 0.61 | Cost: 2 | Best: 0
# Temperature: 0.60 | Cost: 0 | Best: 0
# Temperature: 0.59 | Cost: 2 | Best: 0
# Temperature: 0.59 | Cost: 2 | Best: 0
# Temperature: 0.58 | Cost: 2 | Best: 0
# Temperature: 0.58 | Cost: 2 | Best: 0
# Temperature: 0.57 | Cost: 2 | Best: 0
# Temperature: 0.57 | Cost: 4 | Best: 0
# Temperature: 0.56 | Cost: 2 | Best: 0
# Temperature: 0.55 | Cost: 0 | Best: 0
# Temperature: 0.55 | Cost: 0 | Best: 0
# Temperature: 0.54 | Cost: 0 | Best: 0
# Temperature: 0.54 | Cost: 0 | Best: 0
# Temperature: 0.53 | Cost: 0 | Best: 0
# Temperature: 0.53 | Cost: 0 | Best: 0
# Temperature: 0.52 | Cost: 0 | Best: 0
# Temperature: 0.52 | Cost: 0 | Best: 0
# Temperature: 0.51 | Cost: 0 | Best: 0
# Temperature: 0.51 | Cost: 0 | Best: 0
# Temperature: 0.50 | Cost: 0 | Best: 0
# Temperature: 0.50 | Cost: 0 | Best: 0
# Temperature: 0.49 | Cost: 0 | Best: 0
# Temperature: 0.49 | Cost: 0 | Best: 0
# Temperature: 0.48 | Cost: 0 | Best: 0
# Temperature: 0.48 | Cost: 0 | Best: 0
# Temperature: 0.47 | Cost: 0 | Best: 0
# Temperature: 0.47 | Cost: 0 | Best: 0
# Temperature: 0.46 | Cost: 2 | Best: 0
# Temperature: 0.46 | Cost: 2 | Best: 0
# Temperature: 0.45 | Cost: 2 | Best: 0
# Temperature: 0.45 | Cost: 2 | Best: 0
# Temperature: 0.44 | Cost: 2 | Best: 0
# Temperature: 0.44 | Cost: 2 | Best: 0
# Temperature: 0.44 | Cost: 2 | Best: 0
# Temperature: 0.43 | Cost: 2 | Best: 0
# Temperature: 0.43 | Cost: 2 | Best: 0
# Temperature: 0.42 | Cost: 2 | Best: 0
# Temperature: 0.42 | Cost: 2 | Best: 0
# Temperature: 0.41 | Cost: 2 | Best: 0
# Temperature: 0.41 | Cost: 2 | Best: 0
# Temperature: 0.41 | Cost: 2 | Best: 0
# Temperature: 0.40 | Cost: 2 | Best: 0
# Temperature: 0.40 | Cost: 2 | Best: 0
# Temperature: 0.39 | Cost: 2 | Best: 0
# Temperature: 0.39 | Cost: 2 | Best: 0
# Temperature: 0.39 | Cost: 2 | Best: 0
# Temperature: 0.38 | Cost: 0 | Best: 0
# Temperature: 0.38 | Cost: 0 | Best: 0
# Temperature: 0.37 | Cost: 0 | Best: 0
# Temperature: 0.37 | Cost: 0 | Best: 0
# Temperature: 0.37 | Cost: 0 | Best: 0
# Temperature: 0.36 | Cost: 0 | Best: 0
# Temperature: 0.36 | Cost: 0 | Best: 0
# Temperature: 0.36 | Cost: 0 | Best: 0
# Temperature: 0.35 | Cost: 0 | Best: 0
# Temperature: 0.35 | Cost: 0 | Best: 0
# Temperature: 0.35 | Cost: 0 | Best: 0
# Temperature: 0.34 | Cost: 0 | Best: 0
# Temperature: 0.34 | Cost: 0 | Best: 0
# Temperature: 0.34 | Cost: 0 | Best: 0
# Temperature: 0.33 | Cost: 0 | Best: 0
# Temperature: 0.33 | Cost: 0 | Best: 0
# Temperature: 0.33 | Cost: 0 | Best: 0
# Temperature: 0.32 | Cost: 0 | Best: 0
# Temperature: 0.32 | Cost: 0 | Best: 0
# Temperature: 0.32 | Cost: 0 | Best: 0
# Temperature: 0.31 | Cost: 0 | Best: 0
# Temperature: 0.31 | Cost: 0 | Best: 0
# Temperature: 0.31 | Cost: 0 | Best: 0
# Temperature: 0.30 | Cost: 0 | Best: 0
# Temperature: 0.30 | Cost: 0 | Best: 0
# Temperature: 0.30 | Cost: 0 | Best: 0
# Temperature: 0.29 | Cost: 0 | Best: 0
# Temperature: 0.29 | Cost: 0 | Best: 0
# Temperature: 0.29 | Cost: 0 | Best: 0
# Temperature: 0.29 | Cost: 0 | Best: 0
# Temperature: 0.28 | Cost: 0 | Best: 0
# Temperature: 0.28 | Cost: 0 | Best: 0
# Temperature: 0.28 | Cost: 0 | Best: 0
# Temperature: 0.27 | Cost: 0 | Best: 0
# Temperature: 0.27 | Cost: 0 | Best: 0
# Temperature: 0.27 | Cost: 0 | Best: 0
# Temperature: 0.27 | Cost: 0 | Best: 0
# Temperature: 0.26 | Cost: 0 | Best: 0
# Temperature: 0.26 | Cost: 0 | Best: 0
# Temperature: 0.26 | Cost: 0 | Best: 0
# Temperature: 0.26 | Cost: 0 | Best: 0
# Temperature: 0.25 | Cost: 0 | Best: 0
# Temperature: 0.25 | Cost: 0 | Best: 0
# Temperature: 0.25 | Cost: 0 | Best: 0
# Temperature: 0.25 | Cost: 0 | Best: 0
# Temperature: 0.24 | Cost: 0 | Best: 0
# Temperature: 0.24 | Cost: 0 | Best: 0
# Temperature: 0.24 | Cost: 0 | Best: 0
# Temperature: 0.24 | Cost: 0 | Best: 0
# Temperature: 0.23 | Cost: 0 | Best: 0
# Temperature: 0.23 | Cost: 0 | Best: 0
# Temperature: 0.23 | Cost: 0 | Best: 0
# Temperature: 0.23 | Cost: 0 | Best: 0
# Temperature: 0.22 | Cost: 0 | Best: 0
# Temperature: 0.22 | Cost: 0 | Best: 0
# Temperature: 0.22 | Cost: 0 | Best: 0
# Temperature: 0.22 | Cost: 0 | Best: 0
# Temperature: 0.22 | Cost: 0 | Best: 0
# Temperature: 0.21 | Cost: 0 | Best: 0
# Temperature: 0.21 | Cost: 0 | Best: 0
# Temperature: 0.21 | Cost: 0 | Best: 0
# Temperature: 0.21 | Cost: 0 | Best: 0
# Temperature: 0.20 | Cost: 0 | Best: 0
# Temperature: 0.20 | Cost: 0 | Best: 0
# Temperature: 0.20 | Cost: 0 | Best: 0
# Temperature: 0.20 | Cost: 0 | Best: 0
# Temperature: 0.20 | Cost: 0 | Best: 0
# Temperature: 0.19 | Cost: 0 | Best: 0
# Temperature: 0.19 | Cost: 0 | Best: 0
# Temperature: 0.19 | Cost: 0 | Best: 0
# Temperature: 0.19 | Cost: 0 | Best: 0
# Temperature: 0.19 | Cost: 0 | Best: 0
# Temperature: 0.19 | Cost: 0 | Best: 0
# Temperature: 0.18 | Cost: 0 | Best: 0
# Temperature: 0.18 | Cost: 0 | Best: 0
# Temperature: 0.18 | Cost: 0 | Best: 0
# Temperature: 0.18 | Cost: 0 | Best: 0
# Temperature: 0.18 | Cost: 0 | Best: 0
# Temperature: 0.17 | Cost: 0 | Best: 0
# Temperature: 0.17 | Cost: 0 | Best: 0
# Temperature: 0.17 | Cost: 0 | Best: 0
# Temperature: 0.17 | Cost: 0 | Best: 0
# Temperature: 0.17 | Cost: 0 | Best: 0
# Temperature: 0.17 | Cost: 0 | Best: 0
# Temperature: 0.16 | Cost: 0 | Best: 0
# Temperature: 0.16 | Cost: 0 | Best: 0
# Temperature: 0.16 | Cost: 0 | Best: 0
# Temperature: 0.16 | Cost: 0 | Best: 0
# Temperature: 0.16 | Cost: 0 | Best: 0
# Temperature: 0.16 | Cost: 0 | Best: 0
# Temperature: 0.15 | Cost: 0 | Best: 0
# Temperature: 0.15 | Cost: 0 | Best: 0
# Temperature: 0.15 | Cost: 0 | Best: 0
# Temperature: 0.15 | Cost: 0 | Best: 0
# Temperature: 0.15 | Cost: 0 | Best: 0
# Temperature: 0.15 | Cost: 0 | Best: 0
# Temperature: 0.15 | Cost: 0 | Best: 0
# Temperature: 0.14 | Cost: 0 | Best: 0
# Temperature: 0.14 | Cost: 0 | Best: 0
# Temperature: 0.14 | Cost: 0 | Best: 0
# Temperature: 0.14 | Cost: 0 | Best: 0
# Temperature: 0.14 | Cost: 0 | Best: 0
# Temperature: 0.14 | Cost: 0 | Best: 0
# Temperature: 0.14 | Cost: 0 | Best: 0
# Temperature: 0.13 | Cost: 0 | Best: 0
# Temperature: 0.13 | Cost: 0 | Best: 0
# Temperature: 0.13 | Cost: 0 | Best: 0
# Temperature: 0.13 | Cost: 0 | Best: 0
# Temperature: 0.13 | Cost: 0 | Best: 0
# Temperature: 0.13 | Cost: 0 | Best: 0
# Temperature: 0.13 | Cost: 0 | Best: 0
# Temperature: 0.13 | Cost: 0 | Best: 0
# Temperature: 0.12 | Cost: 0 | Best: 0
# Temperature: 0.12 | Cost: 0 | Best: 0
# Temperature: 0.12 | Cost: 0 | Best: 0
# Temperature: 0.12 | Cost: 0 | Best: 0
# Temperature: 0.12 | Cost: 0 | Best: 0
# Temperature: 0.12 | Cost: 0 | Best: 0
# Temperature: 0.12 | Cost: 0 | Best: 0
# Temperature: 0.12 | Cost: 0 | Best: 0
# Temperature: 0.11 | Cost: 0 | Best: 0
# Temperature: 0.11 | Cost: 0 | Best: 0
# Temperature: 0.11 | Cost: 0 | Best: 0
# Temperature: 0.11 | Cost: 0 | Best: 0
# Temperature: 0.11 | Cost: 0 | Best: 0
# Temperature: 0.11 | Cost: 0 | Best: 0
# Temperature: 0.11 | Cost: 0 | Best: 0
# Temperature: 0.11 | Cost: 0 | Best: 0
# Temperature: 0.11 | Cost: 0 | Best: 0
# Temperature: 0.10 | Cost: 0 | Best: 0
# Temperature: 0.10 | Cost: 0 | Best: 0
# Temperature: 0.10 | Cost: 0 | Best: 0
# Temperature: 0.10 | Cost: 0 | Best: 0
# Temperature: 0.10 | Cost: 0 | Best: 0
# Temperature: 0.10 | Cost: 0 | Best: 0
# ------------------------------
# Final Solution Found:
# Q . . . .
# . . Q . .
# . . . . Q
# . Q . . .
# . . . Q .

# Final Cost: 0
