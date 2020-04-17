# 561. Array Partition 1
# by L.Chong, 4/17/20

# Time   O(nlogn)
# Space: O(N)
# both of these due to python's sort() function

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        i = 0
        result = 0
        
        nums.sort()
        
        while i < len(nums)-1:
            result += min(nums[i], nums[i+1])
            i+=2
        
        return result
