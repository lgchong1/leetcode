# 35. Search Insert Position
# by L. Chong
# Time : O(N)
# Space: O(1)

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        result = 0
        for i in range(len(nums)):
            if nums[i] < target:
                result = i + 1
            if nums[i] == target:
                return i
        return result
