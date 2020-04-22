# 110. Balanced Binary Tree
# by L.Chong 4/22/20

# Time : O(N), every node gets checked
# Space: O(N), a call for every node potentially


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def isBal2(node) -> (int,bool):
            if not node:
                return (0, True)
                       
            lht,lbal = isBal2(node.left)
            rht,rbal = isBal2(node.right)
            
            bal = True if abs(lht-rht) <= 1 else False
            
            return 1+max(lht,rht), lbal and rbal and bal
        
        if not root:
            return True
        
        if not root.left and not root.right:
            return True
        
        lht,lbal = isBal2(root.left)
        rht,rbal = isBal2(root.right)
        
        if not (lbal and rbal):
            return False
        if abs(lht - rht) > 1:
            return False
        return True
    
