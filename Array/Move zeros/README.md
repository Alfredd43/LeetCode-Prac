# Move Zeros

Given an array, move all zeros to the end while keeping the order of non-zero elements.

## Example
Input: `[0, 1, 0, 3, 12]`
Output: `[1, 3, 12, 0, 0]`

## Constraints
- Do it in-place (no extra array)
- Minimize operations

## Approach
Use two pointers: one to track the position for the next non-zero, and one to scan the array. Swap non-zeros forward. 