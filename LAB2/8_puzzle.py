import heapq

# ---------- Heuristics ----------

def misplaced_tiles(state, goal):
    """Count tiles that are not in the correct position (ignore 0)."""
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])


def manhattan_distance(state, goal):
    """Sum of Manhattan distances of tiles from their goal positions."""
    distance = 0
    for i in range(9):
        if state[i] != 0:  # skip blank
            x1, y1 = i // 3, i % 3
            j = goal.index(state[i])
            x2, y2 = j // 3, j % 3
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


# ---------- Puzzle Solver (A*) ----------

def a_star(start, goal, heuristic_func):
    # Priority queue: (f, g, state, path)
    open_list = []
    heapq.heappush(open_list, (heuristic_func(start, goal), 0, start, []))
    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state == goal:
            return path + [state]

        visited.add(tuple(state))

        # Find blank position
        i = state.index(0)
        x, y = i // 3, i % 3

        # Possible moves: up, down, left, right
        moves = [(-1,0), (1,0), (0,-1), (0,1)]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                j = nx * 3 + ny
                new_state = state[:]
                new_state[i], new_state[j] = new_state[j], new_state[i]

                if tuple(new_state) not in visited:
                    h = heuristic_func(new_state, goal)
                    heapq.heappush(open_list, (g+1+h, g+1, new_state, path+[state]))

    return None  # No solution


# ---------- Helper to print board ----------

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# ---------- Example Run ----------

if __name__ == "__main__":
    start = [1,2,3,
             4,0,6,
             7,5,8]

    goal = [1,2,3,
            4,5,6,
            7,8,0]

    print("Solving with Misplaced Tiles Heuristic:")
    solution = a_star(start, goal, misplaced_tiles)
    for step in solution:
        print_board(step)

    print("Solving with Manhattan Distance Heuristic:")
    solution = a_star(start, goal, manhattan_distance)
    for step in solution:
        print_board(step)
