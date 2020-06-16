# 75. Sort Colors
# by. L. Chong
# Time : O(N)
# Space: O(1)


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        
        """
        
        r,w,b = 0,0,0
        for elem in nums:
            if elem == 0:
                r+=1
            elif elem == 1:
                w+=1
            else:
                b+=1
                
        while nums:
            nums.pop()
            
        for _ in range(r):
            nums.append(0)
        for _ in range(w):
            nums.append(1)
        for _ in range(b):
            nums.append(2)
