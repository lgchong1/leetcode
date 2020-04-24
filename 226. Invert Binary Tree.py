# 226. Invert Binary Tree
# by L.Chong, 4/24/20

# Time : O(N)
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def childSwap(node):
            if node:
                node.left,node.right = node.right,node.left
                childSwap(node.left)
                childSwap(node.right)

        childSwap(root)
        return root
