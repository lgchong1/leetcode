# 70. Climbing Stairs
# by L.Chong, 4/27/20

# Time : O(N^2)
# Space: O(N^2)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2) 
