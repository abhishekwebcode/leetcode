# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans=0
        def isLeaf(node):
            return not node.left and not node.right
        def rec(node):
            nonlocal ans
            if not node:
                return
            if node.left and isLeaf(node.left):
                ans+=node.left.val
            else:
                rec(node.left)
            rec(node.right)
        rec(root)
        return ans