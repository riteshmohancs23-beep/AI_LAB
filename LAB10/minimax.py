import math

def print_board(board):
    for row in board:
        print(row)
    print()

def winner(board):
    lines = (
        board[0], board[1], board[2],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    )
    for line in lines:
        if line[0] == line[1] == line[2] != "_":
            return line[0]
    return None

def moves(board):
    m = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                m.append((i, j))
    return m

def minimax(board, depth, is_max):
    w = winner(board)
    if w == "O":
        return 1
    if w == "X":
        return -1
    if not moves(board):
        return 0

    if is_max:
        best = -math.inf
        for (i, j) in moves(board):
            board[i][j] = "O"
            best = max(best, minimax(board, depth + 1, False))
            board[i][j] = "_"
        return best
    else:
        best = math.inf
        for (i, j) in moves(board):
            board[i][j] = "X"
            best = min(best, minimax(board, depth + 1, True))
            board[i][j] = "_"
        return best

def best_move(board):
    best = -math.inf
    move = None
    for (i, j) in moves(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = "_"
        if score > best:
            best = score
            move = (i, j)
    return move

board = [
    ["X", "O", "X"],
    ["_", "O", "_"],
    ["_", "_", "X"]
]

print("Initial Board:")
print_board(board)

m = best_move(board)
board[m[0]][m[1]] = "O"

print("AI Move Played:")
print_board(board)



# Initial Board:
# ['X', 'O', 'X']
# ['_', 'O', '_']
# ['_', '_', 'X']

# AI Move Played:
# ['X', 'O', 'X']
# ['O', 'O', '_']
# ['_', '_', 'X']
