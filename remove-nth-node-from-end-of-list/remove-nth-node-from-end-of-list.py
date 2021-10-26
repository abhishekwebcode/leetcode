# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        removeHead = False
        def rec(node,prev):
            nonlocal n,removeHead
            if not node:
                return 0
            k=1+rec(node.next,node)
            if k==n:
                if prev is None:
                    removeHead = True
                else:
                    prev.next = node.next
            return k
        rec(head,None)
        if removeHead:
            return head.next
        return head