# 206. Reverse Linked List
# 2020-03-21 by L.Chong

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        cur = head
        stack = []

        while cur:
            stack.append(cur.val)
            cur = cur.next

        newHead = ListNode()
        temp = newHead

        while stack:
            temp.val = stack.pop()
            if stack:
                temp.next = ListNode()
                temp = temp.next

        return newHead
