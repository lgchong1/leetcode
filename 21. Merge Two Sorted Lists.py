# 21. Merge Two Sorted Lists
#by L.Chong, 4/26/20

# Time : O(N)
# Space: O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = output = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                output.next = l1
                l1 = l1.next
            else:
                output.next = l2
                l2 = l2.next
            output = output.next

        if l2:
            output.next = l2
        elif l1:
            output.next = l1
            
        return head.next
