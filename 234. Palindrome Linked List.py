# 234. Palindrome Linked List
# by L.Chong, 4/22/20

# Time : O(N)
# Space: O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        count = 0
        
        while (cur):
            count+=1
            cur = cur.next
        
        if count in (0,1):
            return True
        
        myStack = []
        
        cur = head
        i = 0
        
        while i<count/2:
            myStack.append(cur.val)
            i += 1
            cur = cur.next
            
        if count % 2 == 1:
            myStack.pop()
            
        while myStack:
            if myStack.pop() != cur.val:
                return False
            cur = cur.next
            
        return True
