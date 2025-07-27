# Valid Palindrome

## Problem (in simple words)
Given a string, check if it reads the same forwards and backwards, ignoring non-alphanumeric characters and case.

## Example
- Input: "A man, a plan, a canal: Panama"
- Output: True
- Explanation: After removing non-alphanumeric characters and ignoring case, it becomes "amanaplanacanalpanama", which is a palindrome.

## How to Solve (Step by Step)
1. Remove all characters that are not letters or numbers.
2. Convert all letters to lowercase.
3. Use two pointers: one at the start, one at the end.
4. Move both pointers towards the center, checking if characters are the same.
5. If all characters match, return True. If any don't, return False.

## Beginner-Friendly Python Solution
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join(c.lower() for c in s if c.isalnum())
        l = 0
        r = len(result) - 1
        while l < r:
            if result[l] != result[r]:
                return False
            l += 1
            r -= 1
        return True
```

## Constraints
- 1 <= len(s) <= 2 * 10^5
- The string may contain letters, numbers, and symbols. 