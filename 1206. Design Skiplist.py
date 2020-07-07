# 1206. Design Skiplist
# by L. Chong, 6/30/20

import random

DEBUG = True

class Node(object):
    def __init__(self, val=None, next=None, below = None):
        self.val = val
        self.next = next
        self.below = below
        
        if DEBUG: print("Node.__init__({}, {}, {})".format(val,next,below))
            
            
class Skiplist(object):

    def __init__(self):
        self.head = Node()
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
        if DEBUG: print('add({})'.format(num))
        
        heads = self.__numHeads()
        
        if DEBUG: print('\tnum levels  : {}'.format(self.levels))
        if DEBUG: print('\theads rolled: {}'.format(heads))

        if heads > self.levels:
            if DEBUG: print('\t{} rows added'.format(heads-self.levels))
            self.__addRowsAbove(heads - self.levels)
        else:
            if DEBUG: print('\tno rows added')

        skip = self.levels - heads
        if DEBUG: print('\twill add {} to the bottom {} levels and will skip top {} levels'.format(num,heads,skip))

        cur = self.head
        for _ in range(skip):
            cur = cur.below
        while cur:
            self.__addToLevel(cur,num)
            cur = cur.below
        
    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        pass
    
    #HELPERS
    
    def __addRowsAbove(self, times):
        if DEBUG: print('\t__addRowsAbove({})'.format(times))

        for _ in range(times):
            new = Node(None,None,self.head)
            self.head = new
        self.levels += times

    def __addToLevel(self, head, value):
        """Inserts a new node into a level, returning the new node."""

        if DEBUG: print('\t__addToLevel({})'.format(value))

        cur = head
        
        if cur.next == None:
            self.__insert(cur,value)
            return cur
        
        #cur = cur.next

        while cur:
            if cur.next == None or \
                cur.val == value or\
                cur.next.val > value:
                self.__insert(cur,value)
                output = cur
                break
            cur = cur.next
        return output
             
    def __insert(self, node, value):
        """ Inserts a new node after the passed node, returning the new node.

            Given a node and a value, will insert a new node behind the
            parameter node, assigning that new node's val to value. This function
            does no comparisons and assumes input to be modified is intended.

            Args:
                node: a node object after which the new node will be inserted
                value: the value that the new node will assume

            Returns:
                A node whose val will be value and whose next will be node.next
                
                A visualization:

                    Before __insert()

                        node -> node.next

                    After __insert()

                        node -> new -> node.next
                                L>val

        """
        if DEBUG: print('\t__insert({})'.format(value))

        new = Node(value, node.next)
        node.next = new
        return new

    def __numHeads(self):
        """Returns the number of consecutive heads from coin flips (at least 1)."""
        count = 1

        while (self.__coinFlip() == 1):
            count += 1
        return count
        
    def __coinFlip(self):
        rand = int(random.random()*10) % 2
        return rand

    def printList(self):
        # print entire skiplist
        if DEBUG: print("printList()")   
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

    def countRows(self):
        count = 1
        cur = self.head
        while(cur):
            cur = cur.below
            count +=1
        return count

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

if __name__ == "__main__":
    skip = Skiplist()
    skip.printList()
    skip.add(5)
    skip.printList()
    skip.add(6)
    skip.printList()
    skip.add(3)
    skip.printList()
    skip.add(2)
    skip.printList()
