# 121. Best Time to Buy and Sell Stock
# by L.Chong, 4/27/20
# adapted from Leetcode solution

# Time : O(N)
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices:
            minV = prices[0]
        maxP = 0
        
        for i in range(len(prices)):
            if prices[i] < minV:
                minV = prices[i]
            elif prices[i] - minV > maxP:
                maxP = prices[i] - minV
        
        return maxP
