# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def rec(listnode,treenode,match):
            if not treenode:
                return False
            if listnode.val==treenode.val:
                if not listnode.next:
                    return True
                if rec(listnode.next,treenode.left,'match') or rec(listnode.next,treenode.right,'match'):
                    return True
            if match!='match':
                if rec(listnode,treenode.left,'away') or rec(listnode,treenode.right,'away'):
                    return True
            return False
        return rec(head,root,None)