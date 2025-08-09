# Power of Two

## Problem (in simple words)
Given an integer `n`, check if it is a power of two. Return `True` if it is, otherwise return `False`.

A number is a power of two if it can be written as `2^k` for some non-negative integer `k` (like 1, 2, 4, 8, 16, ...).

## Example
- `n = 1` → `True` (because 1 = 2^0)
- `n = 16` → `True` (because 16 = 2^4)
- `n = 3` → `False`
- `n = 0` → `False`
- `n = -4` → `False`

## How to Solve (Step by Step)
1. If `n <= 0`, it's not a power of two → return `False`.
2. While `n` is even (divisible by 2), keep dividing it by 2.
3. After dividing out all factors of 2, check if what's left is exactly `1`.
   - If yes, `n` was a power of two → return `True`.
   - If not, return `False`.

## Beginner-Friendly Python Solution
```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
```

## Constraints
- `-2^31 <= n <= 2^31 - 1`
