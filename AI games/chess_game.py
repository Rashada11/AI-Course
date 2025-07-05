import pygame
import chess
import chess.engine
import os
# === Configuration ===
WIDTH, HEIGHT = 480, 480
SQUARE_SIZE = WIDTH // 8
FPS = 60
WHITE = (245, 245, 220)
BROWN = (139, 69, 19)
STOCKFISH_PATH = r"C:\Users\r chowdhury\Downloads\stockfish-windows-x86-64-avx2.exe"




# === Initialize ===
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess vs Bot")
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Load piece images
pieces_img = {}
pieces_img = {}
for color in ['w', 'b']:
    for piece in ['P', 'R', 'N', 'B', 'Q', 'K']:
        key = piece if color == 'w' else piece.lower()
        path = f"assets/{color}{piece}.png"
        pieces_img[key] = pygame.transform.scale(
            pygame.image.load(path), (SQUARE_SIZE, SQUARE_SIZE)
        )



# === Helper Functions ===
def draw_board(board_obj):
    colors = [WHITE, BROWN]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    for square in chess.SQUARES:
        piece = board_obj.piece_at(square)
        if piece:
            row = 7 - chess.square_rank(square)
            col = chess.square_file(square)
            img = pieces_img[piece.symbol()]
            screen.blit(img, (col*SQUARE_SIZE, row*SQUARE_SIZE))

def get_square_under_mouse():
    x, y = pygame.mouse.get_pos()
    row = 7 - y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return chess.square(col, row)

# === Game Logic ===
def main():
    board = chess.Board()
    engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
    selected_square = None
    running = True

    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))
        draw_board(board)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                engine.quit()
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN and board.turn == chess.WHITE:
                clicked = get_square_under_mouse()

                if selected_square is None:
                    piece = board.piece_at(clicked)
                    if piece and piece.color == chess.WHITE:
                        selected_square = clicked
                else:
                    move = chess.Move(selected_square, clicked)
                    if move in board.legal_moves:
                        board.push(move)
                        selected_square = None
                    else:
                        selected_square = None

        # Bot move
        if not board.turn and not board.is_game_over():
            result = engine.play(board, chess.engine.Limit(time=0.5))
            board.push(result.move)

        if board.is_game_over():
            print("Game Over:", board.result())
            pygame.time.wait(3000)
            running = False
            engine.quit()
            pygame.quit()
            return

if __name__ == "__main__":
    main()
