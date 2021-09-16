class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        leftsum=0
        for i,v in enumerate(nums):
            if leftsum==s-leftsum-v:
                return i
            leftsum+=v
        return -1