from sudoku_puzzle import validate_guess, is_puzzle_solved 
import pytest
import tkinter as tk 
from tkinter import messagebox
from unittest.mock import patch

@pytest.fixture
def puzzle_grid():
    return  [
            [7, 3, 5, 0, 1, 4, 8, 9, 0],
            [0, 4, 2, 0, 7, 3, 5, 0, 1], 
            [9, 0, 0, 2, 0, 5, 3, 7, 4], 
            [0, 8, 6, 3, 4, 0, 1, 5, 7], 
            [0, 0, 3, 8, 0, 7, 0, 2, 6], 
            [5, 7, 9, 0, 2, 0, 4, 0, 8], 
            [1, 0, 7, 4, 0, 2, 6, 0, 3], 
            [6, 0, 0, 7, 3, 8, 0, 1, 5], 
            [3, 2, 0, 5, 0, 1, 7, 4, 9]]


@pytest.fixture
def solution():
    return [
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


@pytest.fixture
def root():
    root = tk.Tk()
    root.withdraw()
    yield root


def test_validate_guess_correct(puzzle_grid, root, solution):

    row = '1'
    col = '3'
    num = '9'
    
    validate_guess(puzzle_grid, root, solution, row, col, num)
    assert puzzle_grid[1][3] == 9


def test_validate_guess_wrong(puzzle_grid, root, solution):

    row = 1
    col = 0
    num = 2
    
    validate_guess(puzzle_grid, root, solution, row, col, num)
    assert puzzle_grid[1][0] == 0


def test_is_puzzle_solved(puzzle_grid, solution, root):
    
    solution = [[1,4,9], [4,8,2]]
    coord_list = [[4,8,2], [1,4,9]]

    with patch('sudoku.messagebox.showinfo') as mock_showinfo:
        is_puzzle_solved(puzzle_grid, solution, coord_list, root)

        mock_showinfo.assert_called_with(message = "Congrats! Puzzle Completed!")


if __name__ == "__main__":
    pytest.main()



