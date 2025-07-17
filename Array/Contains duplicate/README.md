# Contains Duplicate

## Problem (in simple words)
You are given a list of numbers. You need to check if any number appears more than once in the list. If you find any repeated number, return `True`. If all numbers are different, return `False`.

## Example
Suppose you have:
- `nums = [1, 2, 3, 1]`

Let's check for duplicates:
- 1 (first time) — keep going
- 2 (first time) — keep going
- 3 (first time) — keep going
- 1 (already seen!) — so return `True`

Another example:
- `nums = [1, 2, 3, 4]`
- All numbers are different, so return `False`

## How to Solve (Step by Step)
1. Go through each number in the list.
2. Keep track of the numbers you've already seen (use a set for this).
3. For each number, check if you've seen it before.
4. If yes, return `True` (found a duplicate!).
5. If not, remember this number and keep going.
6. If you finish the list without finding any duplicates, return `False`.

## Beginner-Friendly Python Solution
```python
# Function to check for duplicates
# nums: list of numbers

def containsDuplicate(nums):
    seen = set()  # This will store numbers we've seen so far
    for num in nums:
        if num in seen:
            return True  # Found a duplicate!
        seen.add(num)  # Remember this number
    return False  # No duplicates found
```

## Constraints
- The list can have between 1 and 10^5 numbers.
- Each number can be very big or very small (from -10^9 to 10^9). 