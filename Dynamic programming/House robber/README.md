# House Robber

## Problem (in simple words)
You are a professional robber planning to rob houses along a street. Each house has some money stashed, but adjacent houses have security systems connected, so you **cannot rob two adjacent houses**. Given a list of non-negative integers representing the amount of money in each house, find the maximum amount you can rob tonight **without alerting the police**.

## Example
Suppose the houses have money: `[2, 7, 9, 3, 1]`

- If you rob house 0 (money = 2), you cannot rob house 1.
- If you rob house 1 (money = 7), you cannot rob house 0 or 2.
- The best plan is to rob house 0, skip 1, rob 2, skip 3, rob 4: 2 + 9 + 1 = 12.
- But actually, robbing house 1 and 3 gives 7 + 3 = 10, which is less than 12.
- So, the answer is **12**.

## How to Solve (Step by Step)
1. Use two variables to keep track of the max money you can rob up to the previous house and the one before that.
2. For each house, decide: rob it (add its money to the total from two houses ago) or skip it (take the total from the previous house).
3. Take the maximum of these two choices for each house.
4. At the end, the last value is the answer.

## Beginner-Friendly Python Solution
```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
```

## Constraints
- 1 <= number of houses <= 100
- 0 <= money in each house <= 400