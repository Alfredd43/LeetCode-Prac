class Solution(object):
    def moveZeroes(self, nums):
        last_non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[last_non_zero] = nums[last_non_zero], nums[i]
                last_non_zero += 1
        return nums 
sol = Solution()
nums = [0, 1, 0, 3, 12]
print(sol.moveZeroes(nums))