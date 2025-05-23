import math,random
import pygame

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, removed_cells, row_length=9, ):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = 3 
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)] 

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        return self.board
    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        for i in range(self.row_length):
            row = ""
            for j in range(self.row_length):
                num = self.board[i][j]
                if j % 3 == 0 and j != 0:
                    row += "| "
                row += f"{num if num != 0 else '.'} "
            print(row)
            if (i + 1) % 3 == 0 and i != 8:
                print("-" * 21)

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        return num not in self.board[row] # Since there is a list at each row, we use this to check if there is the number already on the list

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        for i in range(self.row_length): # Fro columsns we need to check that the index of the column representing where we are trying to place a number gets checked for every list (every row) because there is no directly a column list
            if self.board[i][col] == num: # [i][col] Here we check i (index) at the specified column (col)
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        for i in range (self.box_length): # We only need to loop through 3 times for a row
            for j in range(self.box_length): # And 3 times for a column
                if self.board[row_start+i][col_start+j] == num: # Unlike the past two functions, neither col nor row are fixed, so here we check for the three numbers in the list for the row and then move to the next row by checking the indexes, row_start only adds after if goes through the columns.
                    return False
        return True

    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        valid = True  # create a true variable boolean

        # If statement to check if the number is in that row, if it is, make the variable false
        if not self.valid_in_row(row, num):
            valid = False

        # If statement to check if the number is in that col, if it is, make the variable false
        if not self.valid_in_col(col, num):
            valid = False

        # If statement to check if the number is in that box, if it is, make the variable false
        box_row_start = row - (row % self.box_length)
        box_col_start = col - (col %self.box_length)
        if not self.valid_in_box(box_row_start,box_col_start,num):
            valid = False
        return valid
    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        for i in range(row_start, row_start + 3): # Checks the three rows in the box
            for j in range(col_start, col_start + 3): # Checks the three columns in the box
                num = random.randint(1, 9) # Generates random number from 1 to 9
                while not self.valid_in_box(row_start, col_start, num):
                    num = random.randint(1, 9) # Checks if the generated number is already in the box, if it is, generates until it is a new number
                self.board[i][j] = num # Replaces 0 with number
    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        for i in range(0, self.row_length - 1, 3):
            self.fill_box(i, i) # Uses fill_box command from earlier to fill the three diagonal boxes

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        x = 0
        while x < self.removed_cells: # Tracks how many removed cells there are until it stops once it reaches the required amount
            rand_row = random.randint(0, 8) # Generates random row
            rand_col = random.randint(0, 8) # Generates random column
            if self.board[rand_row][rand_col] != 0:
                self.board[rand_row][rand_col] = 0 # If no 0 is present already, replaces number with 0
            else:
                continue # If 0 is already present, skips it
            x = x + 1

            pygame.display.update()

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

pygame.init()
screen = pygame.display.set_mode((600, 600))  

# Generating board

sudoku = SudokuGenerator(removed_cells=0)
sudoku.fill_values()
sudoku.remove_cells()
board = sudoku.get_board()

# pygame.init()
# screen = pygame.display.set_mode((600, 600))
#
# # Generating board
#
# sudoku = SudokuGenerator(removed_cells=0)
# sudoku.fill_values()
# board = sudoku.get_board()
#
# run = True
# run2 = True
# while run:
#     for event in pygame.event.get(): # SCreen window loop
#         if event.type == pygame.QUIT:
#             run = False
#
#     screen.fill((255,255,255))
#
#     pygame.display.flip()
#
# def test():
#     sudoku.print_board()
# test()