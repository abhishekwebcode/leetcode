# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        if not head:
            return 0
        nums=set(nums)
        matched=None
        ans=0
        current=head
        while current!=None:
            val=current.val
            if val in nums:
                if not matched:
                    ans+=1
                nums.remove(val)
                matched=True
            else:
                matched=False
            current=current.next
        return ans