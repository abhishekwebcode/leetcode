# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        start = head
        while start is not None:
            while start.next is not None and start.next.val==start.val:
                if start.next.next is None:
                    start.next = None
                else:
                    start.next = start.next.next
            start = start.next
        return head