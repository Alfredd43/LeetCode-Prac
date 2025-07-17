# Plus One

## Problem (in simple words)
You are given a list of digits that together represent a non-negative integer. Imagine the digits are the number's digits in order. Your job is to add 1 to this number and return the new number as a list of digits.

## Example
Suppose you have:
- `digits = [1, 2, 3]` (which means the number 123)

Add one:
- 123 + 1 = 124
- So, return `[1, 2, 4]`

Another example:
- `digits = [9, 9, 9]` (which means the number 999)
- 999 + 1 = 1000
- So, return `[1, 0, 0, 0]`

## How to Solve (Step by Step)
1. Start from the last digit (rightmost).
2. Add 1 to it.
3. If the digit becomes 10, set it to 0 and carry over 1 to the next digit on the left.
4. Repeat until there is no carry left.
5. If you finish all digits and still have a carry, add a new digit (1) at the front.

## Beginner-Friendly Python Solution
```python
# Function to add one to a number represented as a list of digits
# digits: list of digits

def plusOne(digits):
    digits = digits[::-1]  # Reverse for easier addition
    carry, i = 1, 0
    while carry:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                carry = 0
        else:
            digits.append(1)
            carry = 0
        i += 1
    return digits[::-1]  # Reverse back to original order
```

## Constraints
- The list will have at least 1 digit.
- Each digit is between 0 and 9.
- The number does not have leading zeros (except for the number 0 itself). 