# 1290. Convert Binary Number in a Linked List to Integer
# by L.Chong, 4/26/20

# Time : O(N)
# Space: O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        count = 0
        myStack = []
        
        while head:
            myStack.append(head.val)
            head = head.next
            count+=1
        
        final = i = 0
        
        while myStack:           
            if myStack.pop():
                final += pow(2,i)
            i+=1
        
        return final
