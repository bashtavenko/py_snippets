"""15.9 Sudoku solver.

Domain: region = 3 x 3 section
Constraints:
  No dups in rows
  No dups in columns
  All sections contain all numbers from 1 to 9

Ideas:
    Recursive solver with backtracking. Tries all numbers recursively and
    backtracks if that number didn't work.  Check validity on add (row, column,
    region)
"""

import itertools
import math


def solve_sudoku(partial_assignment):
    def solve_partial_sudoku(i, j):
        if i == len(partial_assignment): # len(...) - height
            i = 0 # New row
            j += 1
            if j == len(partial_assignment[i]): # width
                return True # Entire matrix filled without conflict

        # Skips nonempty entries.
        if partial_assignment[i][j] != EMPTY_ENTRY:
            return solve_partial_sudoku(i + 1, j)

        def valid_to_add(i, j, val):
            # Check row constraints
            if any(val == partial_assignment[k][j]
                    for k in range(len(partial_assignment))):
                return False

            # Check column constraint
            if val in partial_assignment[i]:
                return False

            # Check region constraints, meaning 3 x 3 sections
            region_size = int(math.sqrt(len(partial_assignment)))
            I = i // region_size
            J = j // region_size
            return not any(
                    val == partial_assignment[
                        region_size * I + a][region_size * J + b]
                    for a, b in itertools.product(range(region_size), repeat=2))

        for val in range(1, len(partial_assignment) + 1):
            # Try all numbers from 1 to 9
            if valid_to_add(i, j, val):
                partial_assignment[i][j] = val # Try this number
                if solve_partial_sudoku(i + 1, j): # Recursively solve
                    return True

        partial_assignment[i][j] = EMPTY_ENTRY # Backtrack if didn't work
        return False

    EMPTY_ENTRY = 0
    return solve_partial_sudoku(0, 0)
