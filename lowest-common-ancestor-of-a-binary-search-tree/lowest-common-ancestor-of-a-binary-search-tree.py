# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getPath(node,v,arr):
            arr.append(node)
            if node.val==v.val:
                return arr
            if v.val<node.val:
                return getPath(node.left,v,arr)
            return getPath(node.right,v,arr)
        p=getPath(root,p,[])
        q=getPath(root,q,[])
        i=0
        while i<len(p) and i<len(q) and p[i]==q[i]:
            i+=1
        return p[i-1]