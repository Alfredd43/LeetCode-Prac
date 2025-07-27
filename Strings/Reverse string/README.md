# Reverse String

## Problem (in simple words)
You are given a list of characters representing a string. Your job is to reverse the string in-place (that means you should not use extra space for another list) and do it by modifying the input list directly.

## Example
Suppose you have:
- `s = ["h", "e", "l", "l", "o"]`

After reversing, it should become:
- `["o", "l", "l", "e", "h"]`

Another example:
- `s = ["H", "a", "n", "n", "a", "h"]`
- After reversing: `["h", "a", "n", "n", "a", "H"]`

## How to Solve (Step by Step)
1. Use two pointers: one at the start (`l`), one at the end (`r`) of the list.
2. Swap the characters at these two positions.
3. Move the left pointer right (`l += 1`) and the right pointer left (`r -= 1`).
4. Repeat until the two pointers meet or cross.
5. The list is now reversed in-place!

## Beginner-Friendly Python Solution
```python
# Function to reverse the string in-place
# s: list of characters

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return
```

## Constraints
- The list will have at least 1 character and at most 100,000 characters.
- You must reverse the string in-place (no extra list for the answer). 