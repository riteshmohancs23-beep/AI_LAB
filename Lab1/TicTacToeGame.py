import math

def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print()

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[" "]*3 for _ in range(3)]
    print("Welcome to Tic Tac Toe! You are X, Computer is O.\n")
    
    print_board(board)

    while True:
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

play_game()



# #OUTPUT 
# Welcome to Tic Tac Toe! You are X, Computer is O .


#   |   |  
# ---------
#   |   |  
# ---------
#   |   |  

# Enter your move (1-9):  o
# Invalid input! Enter a number between 1-9.
# Enter your move (1-9):  1

# X |   |  
# ---------
#   |   |  
# ---------
#   |   |  

# Computer is thinking...

# X |   |  
# ---------
#   | O |  
# ---------
#   |   |  

# Enter your move (1-9):  4

# X |   |  
# ---------
# X | O |  
# ---------
#   |   |  

# Computer is thinking...

# X |   |  
# ---------
# X | O |  
# ---------
# O |   |  

# Enter your move (1-9):  6

# X |   |  
# ---------
# X | O | X
# ---------
# O |   |  

# Computer is thinking...

# X | O |  
# ---------
# X | O | X
# ---------
# O |   |  

# Enter your move (1-9):  7
# That spot is taken, try again.
# Enter your move (1-9):  3

# X | O | X
# ---------
# X | O | X
# ---------
# O |   |  

# Computer is thinking...

# X | O | X
# ---------
# X | O | X
# ---------
# O | O |  

# Computer wins!
