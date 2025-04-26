import pygame
import sys
from sudoku_generator import SudokuGenerator
def gameWonScreen():
    running = True
    while running:
        screen.fill((255,255,255))

        win_text = bigFont.render("You Won!", True, OceanBlue)
        screen.blit(win_text, (screen_width // 2 - win_text.get_width() // 2, Screen_Height // 2 - win_text.get_height() // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        pygame.display.update()
# pgygame setup
pygame.init()

# Window size
screen_width, Screen_Height = 600, 700
screen = pygame.display.set_mode((screen_width, Screen_Height))
pygame.display.set_caption("Silly Sudoku")

# Colors
milk_white = (255, 255, 255)
voidBlack = (0, 0, 0)
grey_boring = (160, 160, 160)
OceanBlue = (0, 102, 204)
gold_sun = (255, 215, 0)
skyBlue = (173, 216, 230)

# Fonts
bigFont = pygame.font.SysFont("comicsans", 60)
small_font = pygame.font.SysFont("comicsans", 40)

# Buttons for difficulties
easyBox = pygame.Rect(200, 300, 200, 50)
medium_box = pygame.Rect(200, 400, 200, 50)
HardBox = pygame.Rect(200, 500, 200, 50)

def startGame(difficultyLevel):
    playing = True
    selected_row = None
    selectedCol = None

    if difficultyLevel == "easy":
        blanks = 30
    elif difficultyLevel == "medium":
        blanks = 40
    else:
        blanks = 50

    # make the sudoku board
    sudokuMagic = SudokuGenerator(blanks)
    sudokuMagic.fill_values()
    solutionBoard = [row[:] for row in sudokuMagic.get_board()]
    print("Solution:")
    for row in solutionBoard:
        print(row) 
    sudokuMagic.remove_cells()
    myBoard = sudokuMagic.get_board()
    originalBoard = [row[:] for row in myBoard]

    checkBtn = pygame.Rect(200, 660, 200, 30)

    while playing:
        screen.fill(milk_white)

        if selected_row is not None and selectedCol is not None:
            pygame.draw.rect(screen, gold_sun, (50 + selectedCol * 55, 150 + selected_row * 55, 55, 55))

        # draw the lines
        for i in range(10):
            if i % 3 == 0:
                color = OceanBlue
                thickness = 4
            else:
                color = voidBlack
                thickness = 2
            pygame.draw.line(screen, color, (50 + i * 55, 150), (50 + i * 55, 645), thickness)
            pygame.draw.line(screen, color, (50, 150 + i * 55), (545, 150 + i * 55), thickness)

        # draw numbers
        for r in range(9):
            for c in range(9):
                if myBoard[r][c] != 0:
                    if originalBoard[r][c] != 0:
                        num_color = grey_boring
                    else:
                        num_color = voidBlack
                    num_surface = small_font.render(str(myBoard[r][c]), True, num_color)
                    screen.blit(num_surface, (50 + c * 55 + 15, 150 + r * 55 + 10))

        # title
        title = bigFont.render(f"{difficultyLevel.title()} Sudoku", True, voidBlack)
        screen.blit(title, (screen_width // 2 - title.get_width() // 2, 50))

        # check puzzle btn
        pygame.draw.rect(screen, OceanBlue, checkBtn)
        checkText = small_font.render("Check Puzzle", True, milk_white)
        screen.blit(checkText, (checkBtn.x + 10, checkBtn.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if checkBtn.collidepoint(mouse_x, mouse_y):
                    if isBoardFull(myBoard):
                        gameWonScreen()
                        print("Solved it woohoo!")
                    else:
                        print("Nope still missing stuff...")

                if 50 <= mouse_x <= 545 and 150 <= mouse_y <= 645:
                    selectedCol = (mouse_x - 50) // 55
                    selected_row = (mouse_y - 150) // 55

            if event.type == pygame.KEYDOWN:
                if selected_row is not None and selectedCol is not None:
                    if originalBoard[selected_row][selectedCol] == 0:
                        if event.key == pygame.K_1:
                            myBoard[selected_row][selectedCol] = 1
                        if event.key == pygame.K_2:
                            myBoard[selected_row][selectedCol] = 2
                        if event.key == pygame.K_3:
                            myBoard[selected_row][selectedCol] = 3
                        if event.key == pygame.K_4:
                            myBoard[selected_row][selectedCol] = 4
                        if event.key == pygame.K_5:
                            myBoard[selected_row][selectedCol] = 5
                        if event.key == pygame.K_6:
                            myBoard[selected_row][selectedCol] = 6
                        if event.key == pygame.K_7:
                            myBoard[selected_row][selectedCol] = 7
                        if event.key == pygame.K_8:
                            myBoard[selected_row][selectedCol] = 8
                        if event.key == pygame.K_9:
                            myBoard[selected_row][selectedCol] = 9
                        if event.key in [pygame.K_BACKSPACE, pygame.K_DELETE]:
                            myBoard[selected_row][selectedCol] = 0

        pygame.display.update()

    if event.type == pygame.QUIT:
        playing = False
        pygame.quit()
        sys.exit()
def isBoardFull(board):
    for row in board:
        for thingy in row:
            if thingy == 0:
                return False
    return True

def main():
    choosing = True
    Difficulty = None

    while choosing:
        screen.fill(milk_white)
        mouse_pos = pygame.mouse.get_pos()

        # title
        big_title = bigFont.render("Silly Sudoku", True, voidBlack)
        screen.blit(big_title, (screen_width // 2 - big_title.get_width() // 2, 100))

        # draw buttons
        if easyBox.collidepoint(mouse_pos):
            pygame.draw.rect(screen, skyBlue, easyBox)
        else:
            pygame.draw.rect(screen, grey_boring, easyBox)

        if medium_box.collidepoint(mouse_pos):
            pygame.draw.rect(screen, skyBlue, medium_box)
        else:
            pygame.draw.rect(screen, grey_boring, medium_box)

        if HardBox.collidepoint(mouse_pos):
            pygame.draw.rect(screen, skyBlue, HardBox)
        else:
            pygame.draw.rect(screen, grey_boring, HardBox)

        # button text
        easy_label = small_font.render("Easy", True, voidBlack)
        medium_label = small_font.render("Medium", True, voidBlack)
        hard_label = small_font.render("Hard", True, voidBlack)

        screen.blit(easy_label, (easyBox.x + 60, easyBox.y + 5))
        screen.blit(medium_label, (medium_box.x + 35, medium_box.y + 5))
        screen.blit(hard_label, (HardBox.x + 60, HardBox.y + 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easyBox.collidepoint(mouse_pos):
                    Difficulty = "easy"
                    choosing = False
                if medium_box.collidepoint(mouse_pos):
                    Difficulty = "medium"
                    choosing = False
                if HardBox.collidepoint(mouse_pos):
                    Difficulty = "hard"
                    choosing = False

        pygame.display.update()

    if Difficulty:
        startGame(Difficulty)

if __name__ == "__main__":
    main()
