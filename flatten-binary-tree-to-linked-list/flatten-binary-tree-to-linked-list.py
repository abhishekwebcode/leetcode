# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = TreeNode()
        def rec(node):
            nonlocal prev
            if not node:
                return None
            left , right = node.left,node.right
            prev.left = None
            prev.right = node
            prev=node
            rec(left)
            rec(right)
            return node
        rec(root)
        return prev.right