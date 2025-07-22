# Remove Duplicates from Sorted Array

## Problem (in simple words)
You are given a sorted list of numbers. Remove duplicates in-place so each number appears only once. Return the new length. The first part of the list should have the unique numbers in order.

## Example
Suppose you have:
- `nums = [1, 1, 2]`

After removing duplicates:
- Result: `[1, 2, _]` (the underscore means it doesn't matter)
- Return: `2`

## How to Solve (Step by Step)
1. Use a pointer to track where the next unique number should go.
2. Go through the list. If you find a new number, move it forward.
3. Continue until the end. The first part of the list will have all unique numbers.

## Beginner-Friendly Python Solution
```python
# Function to remove duplicates from sorted list
# nums: sorted list of numbers

def removeDuplicates(nums):
    if not nums:
        return 0
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
    return l
```

## Constraints
- The list is sorted.
- Do it in-place (no extra array).
- Return the new length. 