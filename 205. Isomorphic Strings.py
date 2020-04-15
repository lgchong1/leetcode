# 205. Isomorphic Strings.py
# by L. Chong, 4/14/20

# Time : O(N)
# Space: O(N)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        myDict  = {}
        myDict2 = {}
        
        for l,r in zip(s,t):
            if l not in myDict:
                myDict[l] = r
            elif myDict[l] != r:
                return False
            if r not in myDict2:
                myDict2[r] = l
            elif myDict2[r] != l:
                return False
        return True
