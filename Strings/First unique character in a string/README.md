# First Unique Character in a String

## Problem (in simple words)
You are given a string. Find the first character that appears only once in the string. Return its position (index). If no such character exists, return -1.

## Example
Suppose you have the string "leetcode":
- 'l' appears once (at position 0) ✓
- 'e' appears twice (positions 1 and 3) ✗
- 't' appears once (at position 2) ✓
- 'c' appears once (at position 4) ✓
- 'o' appears once (at position 5) ✓
- 'd' appears once (at position 6) ✓

The first unique character is 'l' at position 0.

## How to Solve (Step by Step)
1. Count how many times each character appears in the string.
2. Go through the string again from the beginning.
3. Find the first character that appears only once.
4. Return its position.
5. If no such character exists, return -1.

## Beginner-Friendly Python Solution
```python
from collections import defaultdict

def firstUniqChar(s):
    count = defaultdict(int)
    for c in s:
        count[c] += 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1
```

## Constraints
- The string length is between 1 and 100,000.
- The string contains only lowercase English letters. 