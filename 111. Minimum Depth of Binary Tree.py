# 111. Minimum Depth of Binary Tree.py
# 2020-04-03 by L. Chong

# Time: O(logn)
# Space: O(1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left and root.right:
            return 1 + self.minDepth(root.right)
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.right),
                       self.minDepth(root.left) )
