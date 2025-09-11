# ---------- Depth Limited Search ----------
def dls(node, goal, depth, graph):
    """Depth Limited Search (recursive DFS with depth limit)."""
    if depth == 0 and node == goal:
        return True
    if depth > 0:
        for child in graph.get(node, []):
            if dls(child, goal, depth - 1, graph):
                return True
    return False


# ---------- IDDFS ----------
def iddfs(start, goal, max_depth, graph):
    """Iterative Deepening DFS"""
    for depth in range(max_depth + 1):
        print(f"Searching at depth {depth} ...")
        if dls(start, goal, depth, graph):
            print(f"Goal {goal} found at depth {depth}")
            return True
    print("Goal not found")
    return False


# ---------- Example Run ----------
if __name__ == "__main__":
    # Example tree (like your diagram)
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H', 'I'],
        'E': ['J'],
        'F': ['K'],   # Goal
        'G': [],
        'H': [],
        'I': [],
        'J': [],
        'K': []
    }

    start = 'A'
    goal = 'K'
    iddfs(sta
