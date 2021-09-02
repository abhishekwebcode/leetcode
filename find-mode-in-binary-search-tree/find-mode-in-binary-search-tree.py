# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        a=Counter()
        def rec(r):
            if not r:
                return
            a[r.val]+=1
            rec(r.left)
            rec(r.right)
        rec(root)
        if len(a)==0:
            return []
        m = max(a.values())
        ans=[]
        for key in a:
            if a[key]==m:
                ans.append(key)
        del a
        return ans