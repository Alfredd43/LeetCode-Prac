# Single Number

## Problem (in simple words)
You are given a list of numbers where every number appears exactly twice, except for one number that appears only once. Your job is to find and return that single number.

## Example
Suppose you have:
- `nums = [2, 2, 1]`

Let's look for the single number:
- 2 (first time) — keep going
- 2 (second time) — now both 2s are paired
- 1 (first time, and no pair) — so return `1`

Another example:
- `nums = [4, 1, 2, 1, 2]`
- 4 appears once, 1 and 2 appear twice each, so return `4`

## How to Solve (Step by Step)
1. Go through each number in the list.
2. Use a variable to keep track of the result (start with 0).
3. For each number, use the XOR operation (`^=`) with the result.
4. Numbers that appear twice will cancel each other out (because `a ^ a = 0`).
5. The number that appears only once will be left at the end.

## Beginner-Friendly Python Solution
```python
# Function to find the single number
# nums: list of numbers

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR cancels out pairs
    return result
```

## Constraints
- The list will have at least 1 number and at most 30,000.
- Every number except one appears exactly twice.
- The single number always exists. 