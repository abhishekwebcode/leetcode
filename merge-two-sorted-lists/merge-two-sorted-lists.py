# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        originalPrev = prev
        while l1 and l2:
            if l1.val<l2.val:
                l11 = l1.next
                prev.next = l1
                l1.next=None
                prev=prev.next
                l1 = l11
            else:
                l22 = l2.next
                prev.next = l2
                l2.next=None
                prev=prev.next
                l2 = l22
        if l1:
            prev.next = l1
        if l2:
            prev.next=l2
        return originalPrev.next