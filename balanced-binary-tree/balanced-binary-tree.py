# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        z=True
        def rec(node,h):
            nonlocal z
            h1,h2=h,h
            if node.left:
                h1=rec(node.left,h+1)
            if node.right:
                h2=rec(node.right,h+1)
            if abs(h2-h1)>1:
                z=False
            hww=max(h1,h2)
            return hww
        rec(root,0)
        return z