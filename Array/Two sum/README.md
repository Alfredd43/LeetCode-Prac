# 1. Two Sum

## Problem
Given a list of numbers (`nums`) and a target number (`target`), find the indices of the two numbers in the list that add up to the target. Each input will have exactly one solution, and you cannot use the same element twice.

## Function Signature
```python
def twoSum(nums, target):
    # returns [index1, index2]
```

## Example
- **Input:**
  - nums = [2, 7, 11, 15]
  - target = 13
- **Output:**
  - [0, 2]

### Step-by-step:
- nums[0] = 2
- nums[2] = 11
- 2 + 11 = 13 (which is the target)
- So, return [0, 2]

## Constraints
- 2 <= nums.length <= 10,000
- -1,000,000,000 <= nums[i] <= 1,000,000,000
- -1,000,000,000 <= target <= 1,000,000,000
- Only one valid answer exists for each input. 