# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def rec(node,val):
            if not node:
                return True
            if node.val!=val:
                return False
            return rec(node.left,val) and rec(node.right,val)
        return rec(root,root.val)