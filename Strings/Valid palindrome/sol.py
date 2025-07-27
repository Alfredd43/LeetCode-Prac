class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join(c.lower() for c in s if c.isalnum())
        l = 0
        r = len(result) - 1
        while l<r:
            if result[l] != result[r]:
                return False
            l += 1
            r -= 1
        return True