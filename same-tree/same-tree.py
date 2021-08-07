# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recurse(p,q):
            if (not p ) and (not q):
                return True
            if (p and not q) or (q and not p):
                return False
            if p.val!=q.val:
                return False
            res = True
            if p.left or q.left:
                if p.left and q.left:
                    res = res and recurse(p.left,q.left)
                else:
                    return False
            if p.right or q.right:
                if p.right and q.right:
                    res = res and recurse(p.right,q.right)
                else:
                    return False
            if res == False:
                return False
            return True
        return recurse(p,q)