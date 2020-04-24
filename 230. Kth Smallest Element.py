# 230. Kth Smallest Element in a BST
# by L.Chong, 4/24/20

# Time : O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        elems = []
        
        def tree2list(node, elems):
            
            if not node:
                return
            
            elems.append(node.val)
            tree2list(node.left, elems)
            tree2list(node.right, elems)
            
        tree2list(root,elems)
        
        elems.sort()
        
        #print(elems)
        
        #print(elems[k-1])
        
        return elems[k-1]
