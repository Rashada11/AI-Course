import math

# Initial empty board
board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print(" " + " | ".join(board[i*3:i*3+3]))
        if i < 2:
            print("---+---+---")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_draw(board):
    return all(space != " " for space in board)

def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("❗ That spot is taken.")
        except (ValueError, IndexError):
            print("❗ Invalid input. Please enter a number 1-9.")

def play_game():
    print("\n🎮 Welcome to Tic Tac Toe!")
    print("You are X, AI is O. You go first.")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner(board, "X"):
            print("✅ You win!")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break

        print("🤖 AI is thinking...")
        ai_move()
        print_board()
        if check_winner(board, "O"):
            print("❌ AI wins!")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break

play_game()
