class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for index, num in enumerate(nums):
            diff= target-num
            if diff in seen:
                return [seen[diff],index]
            seen[num] = index   

sol = Solution()

nums = [2, 7, 11, 15]
target = 13
print(sol.twoSum(nums, target))  # Output: [0, 1]
