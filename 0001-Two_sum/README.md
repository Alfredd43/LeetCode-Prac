# Solutions in `sol.py`

## 1. Two Sum

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

- **Method:** `twoSum(nums, target)`
- **Example:**
  - Input: `nums = [2, 7, 11, 15]`, `target = 13`
  - Output: `[0, 2]`
- **Constraints:**
  - 2 <= nums.length <= 10^4
  - -10^9 <= nums[i] <= 10^9
  - -10^9 <= target <= 10^9
  - Only one valid answer exists.

---

## 2. Container With Most Water

Given an integer array `height` of length `n`, find two lines that together with the x-axis form a container, such that the container contains the most water.

- **Method:** `maxArea(height)`
- **Example:**
  - Input: `height = [1,8,6,2,5,4,8,3,7]`
  - Output: `49`
- **Constraints:**
  - 2 <= height.length <= 10^5
  - 0 <= height[i] <= 10^4 