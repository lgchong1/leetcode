# 528. Random Pick with Weight
# by L. Chong
# Time : O()
# Space: O()


import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.arr = []
        
        for i in range(len(w)):
            for _ in range(w[i]):
                self.arr.append(i)
            
        self.len = len(self.arr)
        #print(self.arr)
        #print(self.len)

    def pickIndex(self):
        """
        :rtype: int
        """
        return self.arr[random.randrange(0,self.len)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
