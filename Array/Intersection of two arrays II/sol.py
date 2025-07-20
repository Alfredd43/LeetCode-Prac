class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        counts = Counter(nums1)
        result = []
        
        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1
            
        return result

sol = Solution()
nums1 = [1,2,2,1] 
nums2 = [2,2]
print(sol.intersect(nums1, nums2))