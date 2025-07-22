# Valid Sudoku

## Problem (in simple words)
You are given a 9x9 Sudoku board. Check if it is valid: no repeated numbers in any row, column, or 3x3 box. Empty cells are marked with '.'.

## Example
Suppose you have a board like this (just a small part):
- Row: [5, 3, '.', '.', 7, '.', '.', '.', '.']

If no number repeats in any row, column, or 3x3 box, it's valid.

## How to Solve (Step by Step)
1. For each cell, if it's not '.', check if the number is already in the same row, column, or 3x3 box.
2. If yes, return False.
3. If not, remember the number for that row, column, and box.
4. If you finish, return True.

## Beginner-Friendly Python Solution
```python
import collections

def isValidSudoku(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r // 3, c // 3)]):
                return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
    return True
```

## Constraints
- The board is always 9x9.
- Only digits 1-9 and '.' for empty cells. 