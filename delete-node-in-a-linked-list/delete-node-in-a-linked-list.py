# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        c = node
        while c is not None:
            c.val = c.next.val
            if c.next.next==None:
                c.next=None
                break
            c=c.next
        