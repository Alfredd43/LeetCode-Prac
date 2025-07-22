# Contains Duplicate

## Problem (in simple words)
You are given a list of numbers. Check if any number appears more than once. If yes, return True. If all numbers are different, return False.

## Example
Suppose you have:
- `nums = [1, 2, 3, 1]`
- Result: `True` (because 1 appears twice)

Another example:
- `nums = [1, 2, 3, 4]`
- Result: `False` (all numbers are unique)

## How to Solve (Step by Step)
1. Go through each number in the list.
2. Keep a set of numbers you've seen so far.
3. If you see a number again, return True.
4. If you finish and see no repeats, return False.

## Beginner-Friendly Python Solution
```python
# Function to check for duplicates
# nums: list of numbers

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

## Constraints
- The list will have at least 1 number.
- Each number can be big or small (from -10^9 to 10^9). 