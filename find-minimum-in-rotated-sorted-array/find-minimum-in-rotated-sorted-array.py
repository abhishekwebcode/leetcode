class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if nums[0]<nums[-1]:
            return nums[0]
        l=0
        r=len(nums)-1
        midind=None
        while l<r and l>-1 and r<len(nums):
            prev=midind
            midind = (l+r)//2
            if nums[midind]>nums[midind-1] and nums[midind]>nums[midind+1]:
                return nums[midind+1]
            if nums[midind]<nums[midind-1] and nums[midind]<nums[midind+1]:
                return nums[midind]
            elif nums[midind]>nums[0]:
                l=midind+1
            elif nums[midind]<nums[0]:
                r=midind-1
        print(midind)
        return nums[midind]