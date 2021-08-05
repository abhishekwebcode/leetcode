# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root==None:
            return False
        def isLeaf(currentNode):
            return currentNode.left is None and currentNode.right is None
        def recurse(currentNode,currentSum):
            currentSum = currentSum+currentNode.val
            if isLeaf(currentNode):
                if currentSum==targetSum:
                    return True
            else:
                if currentNode.left:
                    if recurse(currentNode=currentNode.left,currentSum=(currentSum)):
                        return True
                if currentNode.right:
                    if recurse(currentNode=currentNode.right,currentSum=(currentSum)):
                        return True
        return recurse(currentNode=root,currentSum=0)