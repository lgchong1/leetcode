# 237. Delete Node in a Linked List
# by L.Chong, 4/26/20

# Time : O(1)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        node.val  = node.next.val
        node.next = node.next.next