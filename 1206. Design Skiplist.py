# 1206. Design Skiplist
# by L. Chong, 6/30/20 - 7/14/20

import random

DEBUG = False

class Node(object):
    def __init__(self, val=None, next=None, below = None):
        self.val = val
        self.next = next
        self.below = below
        
        #if DEBUG: print("Node.__init__({}, {}, {})".format(val,next,below))
            
            
class Skiplist(object):

    def __init__(self):
        self.head = Node()
        self.levels = 1
        
        #if DEBUG: print("Skiplist instantiated")   
        
    def search(self, target):
        """ Finds if the target is in the Skiplist.
        """
        if DEBUG: print('search({})'.format(target))

        result = False

        cur = self.head
    
        output = "\tPath: "
        
        while cur:
            output += "{}".format(cur.val)
            if not cur.next and not cur.below:
                output += " END"
                break
            elif cur.next == None or\
            target < cur.next.val:
                cur = cur.below
                output += " v "
            elif cur.next.val == target:
                result = True
                output += " -> {}! FOUND".format(target)
                break
            elif target > cur.next.val:
                output += " -> "
                cur = cur.next
            else:
                print("\thow did i get here")

        if DEBUG: print(output)
        if DEBUG: print('\t{}'.format(result))
        return result
        
    def add(self, num):
        """ Adds a new node with the value num in the Skiplist.

            Given a value num, will flip coins and count the number of consecutive
            heads. Will proceed to add a new node with val num to that many levels.
            Each new node will be connected together vertically

            Args:
                num: some numeric value
        """
        if DEBUG: print('add({})'.format(num))
        
        # Calculates how many rows to add if necessary
        
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

        # Starting from the top, determines how many rows to skip before adding in new nodes
      
        cur = self.head
        for _ in range(skip):
            cur = cur.below
    
        col = []        

        # Adds node to each applicable level
        
        while cur:
            new = self.__addToLevel(cur,num)
            col.append(new)
            cur = cur.below

        # Stitches all newly added nodes together across levels
    
        last = None
        while col:
            node = col.pop()
            node.below = last
            last = node        
            
    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        found = False

        cur = self.head

        while cur:
            found = self.__removeFromLevel(cur,num) or found
            cur = cur.below

        if found:
            self.__cleanup()

        return found
    
    #HELPERS
    
    def __addRowsAbove(self, times):
        if DEBUG: print('\t__addRowsAbove({})'.format(times))

        for _ in range(times):
            new = Node(None,None,self.head)
            self.head = new
        self.levels += times

    def __addToLevel(self, head, value):
        """Inserts a new node into a level, returning the new node."""

        #if DEBUG: print('\t__addToLevel({})'.format(value))

        cur = head
        
        if cur.next == None:
            output = self.__insert(cur,value)
            return output
        
        #cur = cur.next

        while cur:
            if cur.next == None or \
                cur.val == value or\
                cur.next.val > value:
                output = self.__insert(cur,value)
                #output = cur
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
        #if DEBUG: print('\t__insert({})'.format(value))

        new = Node(value, node.next)
        node.next = new
        return new

    def __removeFromLevel(self,head,value):
        if DEBUG: print('\t__removeFromLevel({})'.format(value))
        
        cur = head
        
        if cur.next == None:
            return False

        while (cur.next):
            if cur.next.val > value:
                return False
            if cur.next.val == value:
                if DEBUG: print('\t\tremoving {} from level'.format(value))
                self.__removeNext(cur)
                return True
            cur = cur.next      
        
        return False

    def __removeNext(self,node):
        temp = node.next
        node.next = node.next.next
        del temp

    def __numHeads(self):
        """Returns the number of consecutive heads from coin flips (at least 1)."""
        count = 1

        while (self.__coinFlip() == 1):
            count += 1
        return count
        
    def __coinFlip(self):
        return random.choice((0,1))

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
            #if DEBUG: print('\t\tval: {} addr:{} below: {} next: {}'.format(cur.val,cur,cur.below,cur.next))
            level.append(cur.val)
            cur = cur.next

        space = ""
        if DEBUG: space ="\t"
            
        if level:
            print(space + str(level))
        else:
            print(space + "Empty Level")

    '''
    def countRows(self):
        count = 1
        cur = self.head
        while(cur):
            cur = cur.below
            count +=1
        return count
    '''

    def __cleanup(self):
        """Removes empty levels from the top of the Skiplist."""
        while self.levels > 1 and self.head.next == None:
            temp = self.head
            self.head = self.head.below
            del temp
            self.levels -=1

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

def intro():
    print("Skiplist by L.Chong")

def menu(skip):
    while(True):
        print("\nWat do:")
        print("\t1 - add")
        print("\t2 - search")
        print("\t3 - erase")
        print("\t4 - print")

        print("Please choose an option:")
        option = int(input())

        while option not in (1,2,3,4):
            print("Please choose a valid option:")
            option = int(input())
        if option in (1,2,3):
            print("param: ")
            param = int(input())

        if option == 1:
            skip.add(param)
            print("{} added".format(param))
        elif option == 2:
            result = skip.search(param)
            if result:
                print("{} found".format(param))
            else:
                print("{} not found".format(param))
        elif option == 3:
            result = skip.erase(param)
            if result:
                print("{} erased".format(param))
            else:
                print("{} not erased".format(param))
        elif option ==4:
            skip.printList()
        else:
            print("invalid option")
        

if __name__ == "__main__":
    intro()

    skip = Skiplist()

    menu(skip)

    for x in range(16):
        skip.add(x-5)
        skip.printList()

    skip.erase(0)

