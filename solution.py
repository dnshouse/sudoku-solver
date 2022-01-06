from utils import *


def search(values):
    """Using depth-first search and propagation, try all possible values."""
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False  # Failed earlier

    if all(len(values[s]) == 1 for s in boxes):
        return values  # Solved!

    # Choose one of the unfilled squares with the fewest possibilities
    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)

    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:

        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)

        if attempt:
            return attempt


puzzle = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
puzzle2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
puzzle3 = '52...6.........7.13...........4..8..6......5...........418.........3..2...87.....'

grid = grid_values(puzzle3)
grid = search(grid)
display(grid)
