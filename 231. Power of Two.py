# 231. Power of Two
# by L.Chong
# Time : O(logn)
# Space: O()


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        '''
        # Runtime 20ms
        # Mem 12.9MB
        
        
        if n <= 0: return False
        
        def div2(n):
            if n in (1,2): return True
            
            if n % 2 != 0:
                return False
            
            return div2(n/2)
        
        return div2(n)
        
        '''
           
            
        #
        if n <= 0: return False
        
        while(n not in (1,2)):
            if n % 2 != 0:
                return False
            n/=2
            
        return True
