# 1206. Design Skiplist
# by L. Chong, 6/30/20

import random

DEBUG = True
HEADS = 1
TAILS = 0

class Node(object):
    def __init__(self, val=0, next=None, below = None):
        self.val = val
        self.next = next
        self.below = below
        
        if DEBUG: print("New Node:\n\tval: {}\n\tnext val: {}\n\tbelow.val: {}".format(val,next,below))        
            

            
class Skiplist(object):

    def __init__(self):
        self.head = None
        self.levels = 1
        
        if DEBUG: print("Skiplist instantiated")   
        
    def search(self, target):
        """
        :type target: int
        :rtype: bool
        """
        

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        

    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
    #HELPERS
    
    def numHeads(self):
        count = 0
        while (self.coinFlip() == HEADS):
            count += 1
        return count
        
    def coinFlip(self):
        rand = int(random.random()*10) % 2
        return rand
        
# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
