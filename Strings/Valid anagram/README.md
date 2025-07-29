# Valid Anagram

## Problem (in simple words)
Given two strings, check if one string can be rearranged to form the other string. In other words, both strings should contain the same characters with the same frequency.

## Example
- Input: s = "anagram", t = "nagaram"
- Output: True
- Explanation: Both strings contain the same characters: 'a', 'n', 'a', 'g', 'r', 'a', 'm' with the same frequency.

## How to Solve (Step by Step)
1. Check if both strings have the same length. If not, they can't be anagrams.
2. Count the frequency of each character in the first string.
3. Count the frequency of each character in the second string.
4. Compare the character counts. If they match exactly, the strings are anagrams.

## Beginner-Friendly Python Solution
```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

## Alternative Solution (without Counter)
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = {}
        
        # Count characters in first string
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Subtract characters from second string
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        
        return True
```

## Constraints
- 1 <= len(s), len(t) <= 5 * 10^4
- s and t consist of lowercase English letters.