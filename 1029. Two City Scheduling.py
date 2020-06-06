# 1029. Two City Scheduling
# by L. Chong, based on Logan138's explanation
# Time : O(N)
# Space: O(N)

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        minCost = 0
        refund = []
        half = len(costs)//2
        for cost in costs:
            minCost += cost[0]
            refund.append(cost[1]-cost[0])
        
        refund.sort()
        for i in range(half):
            minCost+=refund[i]
            
        return minCost

