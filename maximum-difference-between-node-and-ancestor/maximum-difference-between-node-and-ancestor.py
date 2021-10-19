# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans=0
        def rec(node,mi,ma):
            nonlocal ans,root
            if not node:
                return
            if node!=root:
                ans = max(ans,abs(mi-node.val),abs(ma-node.val))
            mi = min(mi,node.val)
            ma = max(ma,node.val)
            rec(node.left,mi,ma)
            rec(node.right,mi,ma)
        rec(root,float('inf'),float('-inf'))
        return ans