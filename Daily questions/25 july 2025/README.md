# Maximum Unique Subarray Sum After Deletion

## Problem (in simple words)
You are given a list of numbers. You can delete any number of elements (but not all). After deleting, pick a subarray (a contiguous part) where all numbers are unique. What is the biggest sum you can get from such a subarray?

## Example
Suppose you have:
- `nums = [1, 2, 3, 4, 5]`

All numbers are unique, so you can take the whole array.
- Result: `15`

Another example:
- `nums = [1, 1, 0, 1, 1]`

Best you can do is keep one `1` (and/or the `0`).
- Result: `1`

Another example:
- `nums = [1, 2, -1, -2, 1, 0, -1]`

Delete `-1` and `-2`, then pick `[2, 1]`.
- Result: `3`

## How to Solve (Step by Step)
1. If all numbers are negative, just pick the largest (least negative) one.
2. Otherwise, sum all unique non-negative numbers (delete all negatives and duplicates).

## Beginner-Friendly Python Solution
```python
class Solution:
    def maxSum(self, nums):
        s = set()
        m = -float('inf')
        for i in range(len(nums)):
            if nums[i] > 0:
                s.add(nums[i])
            else:
                m = max(m, nums[i])
        if len(s) == 0:
            return m
        res = 0
        for val in s:
            res += val
        return res
```

## Constraints
- The list will have at least 1 number.
- Each number is between -100 and 100.
- You cannot delete all numbers (the array cannot be empty). 