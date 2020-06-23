# 380. Insert Delete GetRandom O(1)
# by L.Chong
'''
  Time:
    constructor: O(1)
    insert     : O(N) 
    remove     : O(N)
    getRandom  : O(1)
'''
# Space: O(N)

import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rSet = [] 

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        
        if val in self.rSet:
            return False
        
        self.rSet.append(val)
        return True
        
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.rSet or not self.rSet:
            return False
        
        last = len(self.rSet) - 1
        if val != self.rSet[last]:
            idx = self.rSet.index(val)
            self.rSet[idx],self.rSet[last] = self.rSet[last],self.rSet[idx]
        self.rSet.pop()
        return True
        
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """

        return random.choice(self.rSet)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
