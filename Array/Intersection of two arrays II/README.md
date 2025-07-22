# Intersection of Two Arrays II

## Problem (in simple words)
You are given two lists of numbers. Find all numbers that appear in both lists, as many times as they appear in both. The result can be in any order.

## Example
Suppose you have:
- `nums1 = [1, 2, 2, 1]`
- `nums2 = [2, 2]`

Result:
- `[2, 2]` (because 2 appears twice in both)

## How to Solve (Step by Step)
1. Count how many times each number appears in the first list.
2. Go through the second list. If a number is in the count, add it to the result and decrease the count.
3. Continue until done.

## Beginner-Friendly Python Solution
```python
from collections import Counter

def intersect(nums1, nums2):
    counts = Counter(nums1)
    result = []
    for num in nums2:
        if counts[num] > 0:
            result.append(num)
            counts[num] -= 1
    return result
```

## Constraints
- Each list will have at least 1 number.
- Numbers can be negative or positive. 