import math

# Function to print the board
def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print()

# Check if someone has won
def check_winner(board, player):
    # Rows and Columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Row
            return True
        if all(board[j][i] == player for j in range(3)):  # Column
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if board is full (draw)
def is_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

# Minimax Algorithm (backtracking)
def minimax(board, depth, is_maximizing):
    # Base cases: check win/lose/draw
    if check_winner(board, "O"):  # Computer wins
        return 1
    if check_winner(board, "X"):  # User wins
        return -1
    if is_full(board):  # Draw
        return 0

    # If it's computer's turn (maximize score)
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":  # Try available move
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)  # Recurse for opponent
                    board[i][j] = " "  # Undo move (backtracking)
                    best_score = max(best_score, score)
        return best_score

    # If it's user's turn (minimize score)
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":  # Try available move
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)  # Recurse for opponent
                    board[i][j] = " "  # Undo move (backtracking)
                    best_score = min(best_score, score)
        return best_score

# Function to find best move for computer
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)  # Simulate user next
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main Game Loop
def play_game():
    board = [[" "]*3 for _ in range(3)]
    print("Welcome to Tic Tac Toe! You are X, Computer is O .\n")
    
    print_board(board)

    while True:
        # User's Move
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                row, col = divmod(move, 3)
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("That spot is taken, try again.")
            except (ValueError, IndexError):
                print("Invalid input! Enter a number between 1-9.")

        print_board(board)

        if check_winner(board, "X"):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # Computer's Move (uses minimax + backtracking)
        print("Computer is thinking...")
        row, col = best_move(board)
        board[row][col] = "O"

        print_board(board)

        if check_winner(board, "O"):
            print("Computer wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Run the game
play_game()
