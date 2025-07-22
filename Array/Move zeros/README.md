# Move Zeros

## Problem (in simple words)
You are given a list of numbers. Move all zeros to the end of the list while keeping the order of the other numbers the same. Do this in-place (don't use a new list).

## Example
Suppose you have:
- `nums = [0, 1, 0, 3, 12]`

After moving zeros:
- Result: `[1, 3, 12, 0, 0]`

## How to Solve (Step by Step)
1. Use a pointer to track where the next non-zero should go.
2. Go through the list. If you find a non-zero, swap it to the front.
3. Keep moving non-zeros forward, zeros naturally go to the end.

## Beginner-Friendly Python Solution
```python
# Function to move all zeros to the end
# nums: list of numbers

def moveZeroes(nums):
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[last_non_zero] = nums[last_non_zero], nums[i]
            last_non_zero += 1
    return nums
```

## Constraints
- The list will have at least 1 number.
- Do it in-place (no extra array).
- Keep the order of non-zero numbers. 