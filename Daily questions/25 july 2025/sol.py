class Solution:
    def maxSum(self, nums):
        s = set()
        m = -float('inf')
        for i in range(len(nums)):
            if nums[i] > 0:
                s.add(nums[i])
            else:
                m = max(m, nums[i])
        
        if len(s) == 0:
            return m
        
        res = 0
        for val in s:
            res += val
        return res
