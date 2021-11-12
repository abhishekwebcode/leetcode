# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode()
        prev=dummy
        current=head
        while current:
            if current.val!=val:
                prev.next=current
                prev=current
            current=current.next
        prev.next = None
        return dummy.next