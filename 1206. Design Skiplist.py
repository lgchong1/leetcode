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
        
    def add2(self,num):
        """
        This is the add to a single linked list
        """
        
        if DEBUG: print("add({})".format(num))   

        newNode = Node(num)
        
        if not self.head:
            if DEBUG: print("\t{} added to head of empty list".format(num))   
            self.head = newNode
        else:
            cur = self.head

            # insert at front
            if num < cur.val:
                if DEBUG: print("\t{} added to head of nonempty list".format(num))   
                self.head = newNode
                newNode.next = cur
                return

            while(cur):
                # end of the list, correct
                if cur.next is None:
                    cur.next = newNode
                    if DEBUG: print("\t{} added at end of list".format(num))   
                    return
                # if new value is greater than next value, keep going
                elif num >= cur.next.val:
                    cur = cur.next
                    return
                # if new value is less than next value, insert
                elif num < cur.next.val:
                    newNode.next = cur.next
                    cur.next = newNode
                    if DEBUG: print("\t{} added in middle of list".format(num))   
                    return
                if DEBUG: print("\tincrement in an unknown spot".format())   
                cur = cur.next

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

    def printList(self):
        # print entire skiplist
        pass

    def printList2(self):
        # print one level of skiplist
        if DEBUG: print("PrintList2()")   
        level = []
    
        cur = self.head

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

    skip.printList2()
    skip.add2(20)
    skip.add2(15)
    skip.add2(1)

    skip.add2(22)
    skip.add2(7)
    skip.add2(0)
    skip.printList2()
