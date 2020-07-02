# 1206. Design Skiplist
# by L. Chong, 6/30/20

import random

DEBUG = True
HEADS = 1
TAILS = 0

class Node(object):
    def __init__(self, val, next=None, below = None):
        self.val = val
        self.next = next
        self.below = below
        
        if DEBUG: print("New Node:\n\tval: {}\n\tnext val:{}\n\tbelow.val: {}".format(val,next,below))        
            
            
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
        result = False

        return result
        
        

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """

        if DEBUG: print('add({})'.format(5))
        
        print('\t' + str(self.__numHeads()))
        

    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
    #HELPERS
    
    def __numHeads(self):
        count = 0

        while (self.__coinFlip() == HEADS):
            count += 1
        return count
        
    def __coinFlip(self):
        rand = int(random.random()*10) % 2
        return rand

    def printList(self):
        # print entire skiplist
        if DEBUG: print("PrintList()")   
        cur = self.head

        while cur:
            self.__printLevel(cur)
            cur = cur.below
        

    def __printLevel(self, head):
        # print one level of skiplist
        level = []

        cur = head

        while cur:
            level.append(cur.val)
            cur = cur.next

        space = ""
        if DEBUG: space ="\t"
            
        if level:
            print(space + str(level))
        else:
            print(space + "Empty Level")


    
# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

if __name__ == "__main__":
    skip = Skiplist()

    for _ in range(10):
        skip.add(5)
