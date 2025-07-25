# Rotate Array

## Problem (in simple words)
You are given a list of numbers and a number k. Rotate the list to the right by k steps. (The last k numbers move to the front.)

## Example
Suppose you have:
- `nums = [1, 2, 3, 4, 5, 6, 7]`
- `k = 3`

After rotating:
- Result: `[5, 6, 7, 1, 2, 3, 4]`

## How to Solve (Step by Step)
1. Reverse the whole list.
2. Reverse the first k numbers.
3. Reverse the rest of the list.

This will rotate the list to the right by k steps, in-place (no extra array).

## Beginner-Friendly Python Solution
```python
class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
```

## Constraints
- The list will have at least 1 number.
- Do it in-place (no extra array). 