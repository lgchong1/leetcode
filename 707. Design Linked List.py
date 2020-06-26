# 707. Design Linked List
# by L. Chong

debug = False


class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
    
        self.head = None
        self.tail = None
        self.len  = 0

        
    def printList(self):
        cur = self.head

        pList = []
        while cur:
            pList.append(cur.val)
            cur = cur.next
        print('list:', pList)
        
    def get(self, index):       
        
        if index >= self.len or index < 0:
            if debug: print('get('+str(index)+'):',-1)
            return -1
        
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            if debug: print('get('+str(index)+'):',cur.val)
            return cur.val
        

    def addAtHead(self, val):
        
        if debug: print('addAtHead('+str(val)+')')
        cur = self.head
        self.head = Node(val,cur)        
        if self.len == 0:
            self.tail = self.head
        self.len +=1        
        if debug: self.printList()

            
            
    def addAtTail(self, val):
        
        if debug: print('addAtTail('+str(val)+')')
        
        if self.len == 0:
            tmp = Node(val)
            self.head = tmp
            self.tail = tmp
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

        self.len +=1
        
        if debug: self.printList()
        

    def addAtIndex(self, index, val):       
        if debug: print('addAtIndex('+str(index)+','+str(val)+')')
              
        if index == 0:
            return self.addAtHead(val)
            
        elif index == self.len:
            return self.addAtTail(val)
        
        elif index < 0 or index > self.len:
            return
        
        else:
            cur = self.head
            for _ in range(index-1):
                cur = cur.next
            if debug: print(cur.val,'to be added after',val)
            temp = Node(val,cur.next)
            cur.next = temp        

            self.len +=1       
        
            if debug: self.printList()

    def deleteAtIndex(self, index):
        if debug: print('delAtIndex('+str(index)+')')
        
        if index >= self.len or index < 0:
            return
        
        #first node
        if index == 0:
            tmp = self.head
            self.head = self.head.next
            del tmp
            self.len -=1
        
        #last node
        elif index == self.len-1:
            cur = self.head
            for _ in range(index-1):
                cur = cur.next     
            self.tail = cur
            cur = cur.next
            if debug: print('attempt to del last value', cur.val)
            self.len-=1
            del cur
            
        elif index >= self.len:
            pass
       
        #middle node
        else:
            cur = self.head
            for _ in range(index-1):
                cur = cur.next
            temp = cur.next
            cur.next = cur.next.next
            self.len -=1
            if debug: print('deleting', temp.val,'at index',index)  
            del temp
      
        if debug: self.printList()
        
