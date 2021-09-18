# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def rec(node):
            ans=str(node.val)
            if not node.left and not node.right:
                return ans
            if node.left:
                ans+="("+rec(node.left)+")"
                if node.right:
                    ans+="("+rec(node.right)+")"
                    return ans
                else:
                    return ans
            else:
                if node.right:
                    ans+="()("+rec(node.right)+")"
                    return ans
                else:
                    return ans
            return ans
        return rec(root)