# 876. Middle of the Linked List
# by L.Chong, 4/26/20

# Time : O(N)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        i = count = 0
        cur = head
        
        while cur:
            cur = cur.next
            count +=1
            
        if count == 1:
            return head
        
        cur = head
               
        while i < count//2:
            cur = cur.next
            i+=1
        
        return cur
