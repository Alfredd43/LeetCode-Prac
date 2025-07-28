# Longest Common Prefix

## Problem (in simple words)
Given a list of strings, find the longest common prefix string that appears at the start of every string. If there is no common prefix, return an empty string.

## Example
Suppose you have these strings:
- ["flower", "flow", "flight"]

The longest common prefix is "fl".

## How to Solve (Step by Step)
1. Start with an empty result string.
2. For each character position in the first string:
   - Check if every string has the same character at that position.
   - If not, return the result so far.
   - If yes, add the character to the result.
3. Return the result after checking all positions.

## Beginner-Friendly Python Solution
```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
```

## Constraints
- 1 <= number of strings <= 200
- 0 <= length of each string <= 200
- Strings contain only lowercase English letters. 