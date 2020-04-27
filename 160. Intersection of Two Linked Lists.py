# 160. Intersection of Two Linked Lists
# by L.Chong, 4/27/20

# Time : O(N)
# Space: O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        output = None
    
        a = []
        b = []
        
        while headA:
            a.append(headA)
            headA = headA.next
        while headB:
            b.append(headB)
            headB = headB.next

        while a and b and a[-1] == b[-1]:
            output = a[-1]
            #print(output)
            a.pop()
            b.pop()
        
        
        return output
