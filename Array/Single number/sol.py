class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
sol = Solution()
nums = [2,2,1]
print (sol.singleNumber(nums))