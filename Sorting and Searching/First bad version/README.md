# First Bad Version

## Problem (in simple words)
You are given versions from 1 to n. One version is the first that is bad, and all versions after it are also bad. Find the first bad version using as few calls to isBadVersion as possible.

## Example
Suppose you have 5 versions, and version 4 is the first bad one:
- isBadVersion(3) -> False
- isBadVersion(4) -> True

So, the answer is 4.

## How to Solve (Step by Step)
1. Use binary search between 1 and n.
2. Check the middle version:
   - If it's bad, the first bad version is at or before this one (move left).
   - If it's good, the first bad version is after this one (move right).
3. Repeat until you find the first bad version.

## Beginner-Friendly Python Solution
```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        l = 1
        r = n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l
```

## Constraints
- 1 <= bad version <= n
- Minimize the number of calls to isBadVersion 