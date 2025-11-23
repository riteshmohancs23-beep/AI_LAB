# alpha_beta.py
move_count = 0

def alpha_beta(depth, node_index, is_maximizing, values, alpha, beta, max_depth):
    global move_count
    move_count += 1

    # If we've reached a leaf, return its value
    if depth == max_depth:
        return values[node_index]

    if is_maximizing:
        best = float('-inf')
        for i in range(2):  # binary tree: left (0) then right (1)
            val = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Pruned at depth {depth} on MAX node {node_index} (child {i})")
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Pruned at depth {depth} on MIN node {node_index} (child {i})")
                break
        return best

def main():
    try:
        max_depth = int(input("Enter the maximum depth of the tree: ").strip())
        if max_depth < 0:
            raise ValueError
    except ValueError:
        print("Error: Please enter a non-negative integer for depth.")
        return

    num_leaves = 2 ** max_depth
    print(f"Enter {num_leaves} leaf node values separated by spaces:")
    try:
        values = list(map(int, input().strip().split()))
    except ValueError:
        print("Error: Please enter integer values for leaves.")
        return

    if len(values) != num_leaves:
        print(f"Error: Number of values does not match 2^{max_depth} = {num_leaves}.")
        return

    global move_count
    move_count = 0
    best_value = alpha_beta(0, 0, True, values, float('-inf'), float('inf'), max_depth)

    print("\nBest value for root (MAX):", best_value)
    print(f"Total moves (nodes visited): {move_count}")

if __name__ == "__main__":
    main()
