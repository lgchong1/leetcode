# 1313. Decompress Run-Length Encoded List
# by L.Chong, 4/26/20

# Time : O(N)
# Space: ???


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        def helper(freq: int, val:int) -> List[int]:
            output = []
            i = 0
            while i < freq:
                output.append(val)
                i+=1
            return output
        
        if not nums:
            return nums
        
        i = 0
        j = len(nums)
        output = []        
        
        while i < j:
            output += helper(nums[i],nums[i+1])            
            i+=2
            
        return output
