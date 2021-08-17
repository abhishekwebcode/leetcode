# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        c=0
        def recurse(node,m):
            nonlocal c
            if node.val>=m:
                c+=1
            m1 = max(node.val,m)
            if node.left:
                recurse(node.left,m1)
            if node.right:
                recurse(node.right,m1)
        recurse(root,float('-inf'))
        return c