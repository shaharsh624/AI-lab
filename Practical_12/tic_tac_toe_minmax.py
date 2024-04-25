import sys


# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print(" - " * 3)


# Function to check if the board is full
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(
        board[i][2 - i] == player for i in range(3)
    ):
        return True
    return False


# Function to evaluate the current state of the board
def evaluate(board):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif is_board_full(board):
        return 0
    else:
        return None


# Minimax algorithm implementation
def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score is not None:
        return score

    if is_maximizing:
        best_score = -sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score


# Function to find the best move for the opponent using Minimax
def find_best_move(board):
    best_score = -sys.maxsize
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


# Main function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player's move
        row, col = map(int, input("Enter your move (row col): ").split())
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = "X"
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        # Opponent's move
        print("Opponent is thinking...")
        opponent_row, opponent_col = find_best_move(board)
        board[opponent_row][opponent_col] = "O"
        print_board(board)
        if check_winner(board, "O"):
            print("Sorry, you lose!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
