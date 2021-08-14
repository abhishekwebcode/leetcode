# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getPath(c,node,path):
            path.append(c)
            if c==node:
                return path
            if c.left:
                ans = getPath(c.left,node,path[:])
                if ans:
                    return ans
            if c.right:
                ans = getPath(c.right,node,path[:])
                if ans:
                    return ans
            return False
        pp = getPath(root,p,[])
        qp = getPath(root,q,[])
        same=root
        while pp and qp:
            if pp[0]==qp[0]:
                same=pp[0]
                del pp[0]
                del qp[0]
            else:
                break
        return same