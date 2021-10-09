# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def it(node):
            if not node:
                return
            yield from it(node.left)
            yield node
            yield from it(node.right)
        nodes = list(it(root))
        for i in range(len(nodes)-1):
            nodes[i].left=None
            nodes[i].right=nodes[i+1]
        nodes[-1].left=None
        nodes[-1].right=None
        return nodes[0]
        
        
            