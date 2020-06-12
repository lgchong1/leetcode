# 392. Is Subsequence
# by L. Chong
# Time : O(len(t))
# Space: O(1)

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i,j = 0,0
        
        if not s: return True
        if not t: return False
        
        if len(s) > len(t):
            return False
        
        
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i+=1
            j+=1
            
        if i != len(s):
            return False
        return True
