# Intersection of Two Arrays II

Given two arrays, return their intersection (each element appears as many times as it shows in both arrays).

## Example
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

## Constraints
- Each array length: 1 to 1000
- Elements: -1000 to 1000

## Approach
Count elements in one array, then for each element in the other, add to result if it appears in both (decrement count). 