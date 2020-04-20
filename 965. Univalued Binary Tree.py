# 965. Univalued Binary Tree
# by L.Chong, 4/20/20

# Time : O(logN)
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        def isSameValue(value, node: TreeNode) -> bool:
            
            # mismatch base case
            if node.val != value:
                return False
            
            # leaf base case
            if not node.left and not node.right:
                return True            
                
            # otherwise, go in
            if node.left and node.right:
                return isSameValue(value, node.left) and \
                       isSameValue(value, node.right)
            elif node.left:
                return isSameValue(value, node.left)
            else:
                return isSameValue(value, node.right)
        
        return isSameValue(root.val, root)
