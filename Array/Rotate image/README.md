# Rotate Image

## Problem (in simple words)
You are given an n x n 2D matrix (a square grid of numbers). Rotate the matrix 90 degrees clockwise, in-place (without using another matrix).

## Example
Suppose you have:
- `matrix = [[1,2,3], [4,5,6], [7,8,9]]`

After rotating 90 degrees clockwise:
- Result: `[[7,4,1], [8,5,2], [9,6,3]]`

## How to Solve (Step by Step)
1. Think of the matrix as layers (like an onion), from the outside in.
2. For each layer, move the numbers in groups of four, swapping them in place.
3. Keep rotating each layer until the whole matrix is done.

## Beginner-Friendly Python Solution
```python
class Solution(object):
    def rotate(self, matrix):
        l, r = 0, len(matrix)-1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                topLeft = matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1
```

## Constraints
- The matrix is always square (n x n).
- Rotate in-place (do not use another matrix). 