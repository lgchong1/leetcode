# 19. Remove Nth Node from End of List
# by L.Chong, 4/23/20

# Time : O(N)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = count = 0
        cur = head
        
        while cur:
            count+=1
            cur = cur.next
            
        # one element base case
        if count == 1:
            return None
        
        # n = first element
        if count == n:
            return head.next
            
        #print('idx to be removed: ', count-n)
        
        cur = head
        
        while i < count-n-1:        #will stop right before node to be removed
            i+=1
            cur = cur.next
            
        #print('value at current elemnt:', cur.val)
        
        cur.next = cur.next.next
        
        return head
