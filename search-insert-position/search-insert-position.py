class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<nums[0]:
            return 0
        if target>nums[-1]:
            return len(nums)
        l = 0
        r=len(nums)-1
        mid=None
        while  l >-1 and r < len(nums) and l<=r:
            mid = int((l+r)/2)
            print([l,r,mid])
            val = nums[mid]
            if val==target:
                return mid
            elif val<target:
                l=mid+1
            else:
                r=mid-1
        if target<nums[mid]:
            return mid
        else:
            return mid+1