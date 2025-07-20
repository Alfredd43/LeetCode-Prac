# Remove Duplicates from Sorted Array

Given a sorted array, remove duplicates in-place and return the new length.

## Example
Input: `[1, 1, 2]`
Output: `2` (array becomes `[1, 2, _]`)

## Constraints
- Do it in-place (no extra array)
- Return the new length
- Elements beyond the new length don't matter

## Approach
Use two pointers: one to track the position for the next unique element, and one to scan the array. Copy unique elements forward. 