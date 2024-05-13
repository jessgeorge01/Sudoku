Project Description: 
A program that generates a Sudoku puzzle that can be played by users. As users input numbers in the boxes, they will receive feedback indicating whether their guess was correct or not. If incorrect, it will give the user another chance to guess. Each time the game is run, it will produce a new board to play. 

Functions: 
A function that uses Tkinter to create the Sudoku game board visual. 
A function that allows users to input their guesses, and checks if the number will correctly fit in the specified box. 
A function that figures out if the board is complete and displays “complete!” on the screen if it is. 

Names of functions and their arguments:
generate_sudoku_puzzle()
display_grid (grid)
validate_guess(grid, row, col, num)
updated_grid(grid)
is_puzzle_solved(grid)

Input data for program should be integers that indicate the row, column, and number that the user wants to put in the empty cell.

Field names: 
Grid: A list of lists with 10 integers 0-9
Row: Integers 0-8 that represent the index of a row in the grid
Col: Integers 0-8 that represent the index of a column in the grid
Num: Integer 1-9 that represents the guess of the user for a specified empty cell

Variable names aren't necessary, but the integers should be entered in the following order: row, col, num
