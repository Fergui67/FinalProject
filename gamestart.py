import pygame
import sys
from sudoku_generator import SudokuGenerator

pygame.init()

WIDTH = 600
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
BLUE = (0, 102, 204)
GOLD = (255, 215, 0)
LIGHT_BLUE = (173, 216, 230)

font_title = pygame.font.SysFont("comicsans", 60)
font_button = pygame.font.SysFont("comicsans", 40)
font_number = pygame.font.SysFont("comicsans", 40)

easy_button = pygame.Rect(200, 300, 200, 50)
medium_button = pygame.Rect(200, 400, 200, 50)
hard_button = pygame.Rect(200, 500, 200, 50)

def start_game(difficulty):
    running = True
    selected_row = None
    selected_col = None

    if difficulty == "easy":
        removed = 30
    elif difficulty == "medium":
        removed = 40
    else:
        removed = 50

    sudoku = SudokuGenerator(9, removed)
    sudoku.fill_values()
    sudoku.remove_cells()
    board = sudoku.get_board()
    original_board = [row[:] for row in board]

    check_button = pygame.Rect(200, 660, 200, 30)

    while running:
        screen.fill(WHITE)

        if selected_row is not None and selected_col is not None:
            highlight_rect = pygame.Rect(50 + selected_col*55, 150 + selected_row*55, 55, 55)
            pygame.draw.rect(screen, GOLD, highlight_rect)

        for i in range(10):
            if i % 3 == 0:
                color = BLUE
                thickness = 4
            else:
                color = BLACK
                thickness = 2
            pygame.draw.line(screen, color, (50 + i*55, 150), (50 + i*55, 150 + 495), thickness)
            pygame.draw.line(screen, color, (50, 150 + i*55), (50 + 495, 150 + i*55), thickness)

        for row in range(9):
            for col in range(9):
                if board[row][col] != 0:
                    if original_board[row][col] != 0:
                        num_color = GREY
                    else:
                        num_color = BLACK
                    num_surface = font_number.render(str(board[row][col]), True, num_color)
                    num_rect = num_surface.get_rect(center=(50 + col*55 + 27, 150 + row*55 + 27))
                    screen.blit(num_surface, num_rect)

        title_text = font_title.render(f"{difficulty.title()} Sudoku", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 50))
        screen.blit(title_text, title_rect)

        pygame.draw.rect(screen, BLUE, check_button)
        check_text = font_button.render("Check Puzzle", True, WHITE)
        screen.blit(check_text, (check_button.x + 10, check_button.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if check_button.collidepoint(mouse_x, mouse_y):
                    if check_board(board):
                        print("Puzzle solved correctly!")
                    else:
                        print("Puzzle not solved yet.")

                if 50 <= mouse_x <= 545 and 150 <= mouse_y <= 645:
                    selected_col = (mouse_x - 50) // 55
                    selected_row = (mouse_y - 150) // 55

            if event.type == pygame.KEYDOWN:
                if selected_row is not None and selected_col is not None:
                    if original_board[selected_row][selected_col] == 0:
                        if event.key == pygame.K_1:
                            board[selected_row][selected_col] = 1
                        if event.key == pygame.K_2:
                            board[selected_row][selected_col] = 2
                        if event.key == pygame.K_3:
                            board[selected_row][selected_col] = 3
                        if event.key == pygame.K_4:
                            board[selected_row][selected_col] = 4
                        if event.key == pygame.K_5:
                            board[selected_row][selected_col] = 5
                        if event.key == pygame.K_6:
                            board[selected_row][selected_col] = 6
                        if event.key == pygame.K_7:
                            board[selected_row][selected_col] = 7
                        if event.key == pygame.K_8:
                            board[selected_row][selected_col] = 8
                        if event.key == pygame.K_9:
                            board[selected_row][selected_col] = 9
                        if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                            board[selected_row][selected_col] = 0

        pygame.display.update()

    pygame.quit()
    sys.exit()
def check_board(board):
    for row in board:
        for num in row:
            if num == 0:
                return False
    return True

def main():
    running = True
    selected_difficulty = None

    while running:
        screen.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()

        title_text = font_title.render("Sudoku", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 100))
        screen.blit(title_text, title_rect)

        if easy_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, LIGHT_BLUE, easy_button)
        else:
            pygame.draw.rect(screen, GREY, easy_button)

        if medium_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, LIGHT_BLUE, medium_button)
        else:
            pygame.draw.rect(screen, GREY, medium_button)

        if hard_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, LIGHT_BLUE, hard_button)
        else:
            pygame.draw.rect(screen, GREY, hard_button)

        easy_text = font_button.render("Easy", True, BLACK)
        medium_text = font_button.render("Medium", True, BLACK)
        hard_text = font_button.render("Hard", True, BLACK)

        screen.blit(easy_text, (easy_button.x + 50, easy_button.y + 5))
        screen.blit(medium_text, (medium_button.x + 30, medium_button.y + 5))
        screen.blit(hard_text, (hard_button.x + 50, hard_button.y + 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(mouse_pos):
                    selected_difficulty = "easy"
                    running = False
                if medium_button.collidepoint(mouse_pos):
                    selected_difficulty = "medium"
                    running = False
                if hard_button.collidepoint(mouse_pos):
                    selected_difficulty = "hard"
                    running = False

        pygame.display.update()

    if selected_difficulty:
        start_game(selected_difficulty)

if __name__ == "__main__":
    main()
