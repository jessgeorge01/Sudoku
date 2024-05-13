import random
import tkinter as tk 
from tkinter import messagebox

def sudoku_puzzle_solved():
	# shows a completed sudoku board for reference
	# not used in code that is ran

	puzzle_grid = [
					[7, 3, 5, 6, 1, 4, 8, 9, 2],
					[8, 4, 2, 9, 7, 3, 5, 6, 1], 
					[9, 6, 1, 2, 8, 5, 3, 7, 4], 
					[2, 8, 6, 3, 4, 9, 1, 5, 7], 
					[4, 1, 3, 8, 5, 7, 9, 2, 6], 
					[5, 7, 9, 1, 2, 6, 4, 3, 8], 
					[1, 5, 7, 4, 9, 2, 6, 8, 3], 
					[6, 9, 4, 7, 3, 8, 2, 1, 5], 
					[3, 2, 8, 5, 6, 1, 7, 4, 9]]


def generate_sudoku_puzzle():
	# sudoku board set up for game
	# 0's represent empty cells that users are supposed to fill

	puzzle_grid = [
					[7, 3, 5, 0, 1, 4, 8, 9, 0],
					[0, 4, 2, 0, 7, 3, 5, 0, 1], 
					[9, 0, 0, 2, 0, 5, 3, 7, 4], 
					[0, 8, 6, 3, 4, 0, 1, 5, 7], 
					[0, 0, 3, 8, 0, 7, 0, 2, 6], 
					[5, 7, 9, 0, 2, 0, 4, 0, 8], 
					[1, 0, 7, 4, 0, 2, 6, 0, 3], 
					[6, 0, 0, 7, 3, 8, 0, 1, 5], 
					[3, 2, 0, 5, 0, 1, 7, 4, 9]]

	return puzzle_grid


# solution for the sudoku board
# numbers are written as [row, column, number]
# organized by row

solution = [
			[0,3,6], [0,8,2], 
			[1,0,8], [1,3,9], [1,7,6], 
			[2,1,6], [2,2,1], [2,4,8],
			[3,0,2], [3,5,9], 
			[4,0,4], [4,1,1], [4,4,5], [4,6,9], 
			[5,3,1], [5,5,6], [5,7,3], 
			[6,1,5], [6,4,9], [6,7,8], 
			[7,1,9], [7,2,4], [7,6,2], 
			[8,2,8], [8,4,6]
			]


def display_grid(puzzle_grid, root):
	# displays the sudoku board set up onto the tk window

	x = 15
	y = 120

	for lists in puzzle_grid:
		y += 20
		new_label = tk.Label(root, text = lists)
		new_label.place(x = x, y = y)


def get_guess(puzzle_grid, root): # got from textbook
	# allows users to interact with board and type in their guesses

	tk.Label(root, text="Start counting rows/columns from 0. Example: first row = 0, second row = 1, etc.").grid(row=0)
	# explains how to count the rows/columns properly for code to work

	tk.Label(root, text="Row").grid(row=1)
	tk.Label(root, text="Column").grid(row=2)
	tk.Label(root, text="Number").grid(row=3)
	# creates labels in the window for users 

	row_entry = tk.Entry(root, fg = "black", bg="white")
	row_entry.grid(row=1, column=1)
	# creates an entry box for users to type in the desired row number

	column_entry = tk.Entry(root, fg = "black", bg="white")
	column_entry.grid(row=2, column=1)
	# creates an entry box for users to type in the desired column number

	number_entry = tk.Entry(root, fg = "black", bg="white")
	number_entry.grid(row=3, column=1)
	# creates an entry box for users to type in the desired guess number

	return row_entry, column_entry, number_entry


def get_entry_data(puzzle_grid, root, entries): # got from textbook
	# retrieves the information that users input to store for later use

	row_entry, column_entry, number_entry = entries
	
	row = row_entry.get()
	col = column_entry.get()
	num = number_entry.get()

	return(row, col, num)
	

# creates a nested list to store correct user guesses
# stores each guess as a list organized as [row, column, number]
coord_list = [] 


def validate_guess(puzzle_grid, root, solution, row, col, num):
	# checks if the user's guess is correct by comparing it to the sublists in the solution list

	for sub in solution: # iterates through each sublist
		if row == str(sub[0]): # checks if the row matches the row in any sublist
			if col == str(sub[1]): # checks if the column matches the column in the sublist
				if num == str(sub[2]): # checks if the guessed number matches the number in the sublist
					
					if [int(row), int(col), int(num)] not in coord_list: # runs if guess wasn't already inputted by user
						messagebox.showinfo(message = "Correct solution! Input your next guess.") # creates pop up window 
						
						coord_list.append([int(row), int(col), int(num)]) # adds verified guess into the nested list
						puzzle_grid[int(row)][int(col)] = int(num) # updates the sudoku board to replace empty cell with the verified guess
						display_grid(puzzle_grid, root)
						return

					elif [int(row), int(col), int(num)] in coord_list: # runs if guess was already inputted by user 
						messagebox.showinfo(message = "Correct! Already guessed, try another one!") # creates pop up window
				
				else: # runs if guess is incorrect and isn't in the solution list
					messagebox.showinfo(message = "Incorrect! Try again!") # creates pop up window


def submit_guess(puzzle_grid, root, entries, coord_list):
	
	row, col, num = get_entry_data(puzzle_grid, root, entries)
	# stores the get_entry_data results into appropriate variables

	validate_guess(puzzle_grid, root, solution, row, col, num)
	# runs the validate_guess function


def is_puzzle_solved(puzzle_grid, solution, coord_list, root):
	# checks to see if sudoku board is complete

	final_solution = sorted(solution) # sorts solution 
	final_coord = sorted(coord_list) # sorts verified user guesses
	# sorts the solution list and coord_list so that the sublists are in the same order for both
	
	if final_coord == final_solution: # runs if the user guesses and solution lists are the same
		messagebox.showinfo(message = "Congrats! Puzzle Completed!") # creates pop up window
		root.destroy() # terminates window since game is complete
	else: 
		messagebox.showinfo(message = "Not Quite! Keep Going!") # creates pop up window


def main():
    puzzle_grid = generate_sudoku_puzzle() # assigns variable to sudoku board
    root = tk.Tk() # runs tkinter GUI
    display_grid(puzzle_grid,root) # display sudoku board
    entries = get_guess(puzzle_grid,root) # assigns variable to user input
    submit_button = tk.Button(root, text = 'Submit', command = lambda: submit_guess(puzzle_grid, root, entries, coord_list)) # creates button to submit guess
    submit_button.grid(row = 4, columnspan = 3) # organizes button placing on window
    done_button = tk.Button(root, text = 'Done', command = lambda: is_puzzle_solved(puzzle_grid, solution, coord_list, root)) # creates button to check if puzzle is complete
    done_button.grid(row = 5, columnspan = 3) # organizes button placing on window
    root.mainloop() # keeps tkinter GUI running


if __name__ == "__main__":
    main()

