# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def rec(node,s):
            v=s*10+node.val
            if not node.right and not node.left:
                return v
            else:
                ans=0
                if node.left:
                    ans+=rec(node.left,v)
                if node.right:
                    ans+=rec(node.right,v)
                return ans
        return rec(root,0)