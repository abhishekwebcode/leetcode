# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root==None:
            return []
        paths=[]
        def isLeaf(currentNode):
            return currentNode.left is None and currentNode.right is None
        def recurse(currentNode,currentPath,currentSum):
            currentSum = currentSum+currentNode.val
            currentPath.append(currentNode.val)
            if isLeaf(currentNode):
                if currentSum==targetSum:
                    paths.append(currentPath)
            else:
                if currentNode.left:
                    recurse(currentNode=currentNode.left,currentPath=list(currentPath),currentSum=int(currentSum))
                if currentNode.right:
                    recurse(currentNode=currentNode.right,currentPath=list(currentPath),currentSum=int(currentSum))
        recurse(currentNode=root,currentPath=[],currentSum=0)
        return paths