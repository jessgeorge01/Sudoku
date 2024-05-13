# Project Description: 

A program that generates a Sudoku puzzle that can be played by users. Empty cells will be represented by a '0'. As users input numbers in the provided entry boxes, they will receive feedback indicating whether their guess was correct or not. If incorrect, it will give the user another chance to guess. Once users are done, users can click the 'Done' button to check if the board is complete or if there are any remaining empty cells.

# Functions: 

A function that uses Tkinter to create the Sudoku game board visual. 
A function that allows users to input their guesses, and checks if the number will correctly fit in the specified box. 
A function that figures out if the board is complete and displays “complete!” on the screen if it is. 

## Names of functions and their arguments:

### generate_sudoku_puzzle():
* 0’s represent empty cells that the users are supposed to fill
* returns the puzzle grid that will be displayed to users

### display_grid(puzzle_grid, root):
* displays grid using Tkinter
* puzzle_grid argument: the sudoku grid that is generated in the first function

### get_guess(puzzle_grid, root): 
* allows users to interact with board and type in their guesses
* creates labels in the window for users
* creates an entry box for users to type in the desired row, column, and guess number

### get_entry_data(puzzle_grid, root, entries):
* retrieves the information that users input to store for later us

### validate_guess(puzzle_grid, root, solution, row, col, num):
* checks if the user's guess is correct by comparing it to the sublists in the solution list
* adds verified guess into the nested list of user guesses
* updates the sudoku board to replace empty cell with the verified guess
* Has pop up windows to tell users if guess is right, repeated, or wrong

### submit_guess(puzzle_grid, root, entries, coord_list):
* stores the get_entry_data results into appropriate variables
* runs the validate_guess function

### is_puzzle_solved(puzzle_grid, solution, coord_list, root):
* checks to see if sudoku board is complete
* sorts the solution list and coord_list so that the sublists are in the same order for both
* Has pop up windows that say if puzzle is complete or not
* If complete, tkinter window terminates

## Field names: 

### Row: 
Integers 0-8 that represent the index of a row in the grid
### Col: 
Integers 0-8 that represent the index of a column in the grid
### Num: 
Integer 1-9 that represents the guess of the user for a specified empty cell
