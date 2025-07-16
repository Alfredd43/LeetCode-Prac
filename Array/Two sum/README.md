# 1. Two Sum

## Problem (in simple words)
You are given a list of numbers and a target number. Your job is to find two different numbers in the list that add up to the target. You need to return the positions (indices) of these two numbers.

- You can't use the same number twice.
- There is always exactly one answer.

## Example
Suppose you have:
- `nums = [2, 7, 11, 15]`
- `target = 13`

Let's look for two numbers that add up to 13:
- 2 + 7 = 9 (no)
- 2 + 11 = 13 (yes!)

So, the answer is the indices of 2 and 11, which are `[0, 2]`.

## How to Solve (Step by Step)
1. Go through each number in the list.
2. For each number, figure out what number you need to reach the target (target - current number).
3. Check if you've already seen that needed number before.
4. If yes, return the indices.
5. If not, remember the current number and its index for later.

## Beginner-Friendly Python Solution
```python
# Function to solve Two Sum
# nums: list of numbers
# target: the number we want to get by adding two numbers from nums

def twoSum(nums, target):
    seen = {}  # This will store numbers we've seen so far and their indices
    for index, num in enumerate(nums):
        needed = target - num  # The number we need to find
        if needed in seen:
            return [seen[needed], index]  # Found the answer!
        seen[num] = index  # Remember this number and where we saw it
```

## Constraints
- The list will have at least 2 numbers and at most 10,000.
- Numbers can be very big or very small (from -1,000,000,000 to 1,000,000,000).
- There is always one solution. 