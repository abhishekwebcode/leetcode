from copy import deepcopy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def recursiveBuild(subTreeArray):
            if not subTreeArray:
                return [None]
            treesAtThisLevel=[]
            for i in range(len(subTreeArray)):
                root=subTreeArray[i]
                leftTrees=recursiveBuild(subTreeArray[:i])
                rightTrees=recursiveBuild(subTreeArray[i+1:])
                allLeftSubtrees=[]
                for leftTree in leftTrees:
                    allLeftSubtrees.append(TreeNode(root,leftTree))
                allTrees=[]
                # cartesian product (cross product) 
                # of all left subtrees with right subtrees to get all combinations
                # getting us all the possible trees for 
                # this selected *root* including those with null
                for rightTree in rightTrees:
                    for leftTree in allLeftSubtrees:
                        subTree=deepcopy(leftTree)
                        subTree.right=deepcopy(rightTree)
                        allTrees.append(subTree)
                treesAtThisLevel.extend(allTrees)
            return treesAtThisLevel
        return recursiveBuild(list(range(1,n+1)))