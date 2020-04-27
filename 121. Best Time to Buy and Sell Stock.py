# 121. Best Time to Buy and Sell Stock
# by L.Chong, 4/27/20

# Time : O(N^2)
# Space: O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def findLargest(nums: List[int]) -> int:
            maxV = nums[0]
            
            for elem in nums:
                if elem > maxV:
                    maxV = elem
                    
            return maxV
        
        maxs = []
        lastMax = 0
        
        for i in range(len(prices)-1):
            if i > 0 and maxs[i-1] > prices[i]:
                maxs.append(maxs[i-1])
            else:
                maxs.append(findLargest(prices[1+i:]))
        maxs.append(0)
        
        print(prices)
        print(maxs)
        
        maxProfit = 0
        
        for i in range(len(prices)):
            if maxs[i] - prices[i] > maxProfit:
                maxProfit = maxs[i] - prices[i]
                
        return maxProfit
