# 905. Sort Array By Parity
# by L. Chong, 4/17/20

# Time : O(N)
# Space: O(1)

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) in (0,1):
            return A
        
        lptr = 0
        rptr = len(A) - 1
        
        while lptr <= rptr:
            while lptr < len(A) and A[lptr] % 2 == 0:
                lptr += 1
            while rptr >= 0     and A[rptr] % 2 == 1:
                rptr -= 1
            if lptr <= rptr:
                A[lptr],A[rptr] = A[rptr],A[lptr]
                
        return A
