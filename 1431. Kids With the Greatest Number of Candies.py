# 1431. Kids With the Greatest Number of Candies
# by L. Chong
# Time : O(N)
# Space: O(N)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        maxC = 0
        for elem in candies:
            if elem > maxC:
                maxC = elem
                
        for elem in candies:
            if elem + extraCandies >= maxC:
                output.append(True)
            else:
                output.append(False)
                
        return output
