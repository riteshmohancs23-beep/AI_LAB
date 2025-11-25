from collections import deque

def to_tuple(state):
    return tuple(state)

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

def get_neighbors(state):
    neighbors = []
    blank = state.index(0)

    moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7]
    }

    for m in moves[blank]:
        new_state = list(state)
        new_state[blank], new_state[m] = new_state[m], new_state[blank]
        neighbors.append(new_state)

    return neighbors

def dfs(state, goal, visited):

    if state == goal:
        return [state]

    visited.add(to_tuple(state))

    for neighbor in get_neighbors(state):

        neighbor_t = to_tuple(neighbor)

        if neighbor_t not in visited:

            path = dfs(neighbor, goal, visited)
            if path:
                return [state] + path

    return None

def solve_8_puzzle_dfs(start, goal):
    visited = set()
    path = dfs(start, goal, visited)

    if path:
        for step in path:
            print_board(step)
    else:
        print("No solution found.")

    return path


start_state = [1, 2, 3,
               4, 5, 6,
               7, 0, 8]

goal_state  = [1, 2, 3,
               4, 5, 6,
               7, 8, 0]

solve_8_puzzle_dfs(start_state, goal_state)
