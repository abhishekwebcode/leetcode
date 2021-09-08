# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        arr=nums
        def makeTree(i,j):
            if i==j:
                return None
            mid=(i+j)//2
            left=makeTree(i,mid)
            right=makeTree(mid+1,j)
            return TreeNode(nums[mid],left,right)
        return makeTree(0,len(nums))