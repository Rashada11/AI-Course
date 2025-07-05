import random
import copy

SIZE = 5
TREASURES = 5
TRAPS = 5
SIMULATIONS_PER_TILE = 20

def generate_board():
    board = [["?" for _ in range(SIZE)] for _ in range(SIZE)]
    contents = ["T"] * TREASURES + ["X"] * TRAPS + [" "] * (SIZE*SIZE - TREASURES - TRAPS)
    random.shuffle(contents)
    hidden = [contents[i * SIZE:(i + 1) * SIZE] for i in range(SIZE)]
    return board, hidden

def print_board(board):
    print("\n   " + " ".join(map(str, range(SIZE))))
    for i, row in enumerate(board):
        print(f"{i}  " + " ".join(row))

def valid_cells(revealed):
    return [(i, j) for i in range(SIZE) for j in range(SIZE) if not revealed[i][j]]

def simulate_score(board, hidden, revealed, x, y):
    # Simulate picking tile (x, y) and then finishing game randomly
    total_score = 0
    for _ in range(SIMULATIONS_PER_TILE):
        sim_revealed = [row[:] for row in revealed]
        sim_hidden = [row[:] for row in hidden]
        score = 0
        options = valid_cells(sim_revealed)
        random.shuffle(options)
        options.insert(0, (x, y))  # Try this one first

        for cx, cy in options:
            if sim_revealed[cx][cy]:
                continue
            tile = sim_hidden[cx][cy]
            sim_revealed[cx][cy] = True
            if tile == "T":
                score += 1
            elif tile == "X":
                score -= 1
        total_score += score
    return total_score / SIMULATIONS_PER_TILE

def ai_pick(board, hidden, revealed):
    options = valid_cells(revealed)
    best_score = float("-inf")
    best_move = None
    for x, y in options:
        score = simulate_score(board, hidden, revealed, x, y)
        if score > best_score:
            best_score = score
            best_move = (x, y)
    return best_move

def reveal(x, y, board, hidden, revealed, scores, player):
    revealed[x][y] = True
    tile = hidden[x][y]
    board[x][y] = tile
    if tile == "T":
        scores[player] += 1
        print(f"{player} found TREASURE!")
    elif tile == "X":
        scores[player] -= 1
        print(f"{player} triggered a TRAP!")
    else:
        print(f"{player} found nothing.")

# Game loop
board, hidden = generate_board()
revealed = [[False]*SIZE for _ in range(SIZE)]
scores = {"You": 0, "AI": 0}
turn = 0

print("🔍 Welcome to Treasure Trap with Monte Carlo AI!")

while any("?" in row for row in board):
    print_board(board)
    print(f"\nScore — You: {scores['You']} | AI: {scores['AI']}\n")

    if turn % 2 == 0:
        try:
            x, y = map(int, input("Your move (row col): ").split())
            if (x, y) not in valid_cells(revealed):
                print("❌ Invalid or already revealed. Try again.")
                continue
        except:
            print("⚠️ Please enter two integers like '2 3'.")
            continue
        reveal(x, y, board, hidden, revealed, scores, "You")
    else:
        print("🤖 AI is analyzing the board...")
        x, y = ai_pick(board, hidden, revealed)
        print(f"AI selects ({x}, {y})")
        reveal(x, y, board, hidden, revealed, scores, "AI")

    turn += 1

# Final result
print_board(board)
print(f"\n🏁 Final Score — You: {scores['You']} | AI: {scores['AI']}")
if scores["You"] > scores["AI"]:
    print("🎉 You win!")
elif scores["You"] < scores["AI"]:
    print("💀 AI wins!")
else:
    print("🤝 It's a tie!")
