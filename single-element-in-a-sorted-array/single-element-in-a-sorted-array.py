class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        hi = len(nums)-1
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
        def getLast(ind):
            if nums[ind]==nums[ind-1]:
                return ind
            if nums[ind+1]==nums[ind]:
                return ind+1
        while low<=hi:
            mid = (hi+low)//2
            i = getLast(mid)
            if i is None:
                return nums[mid]
            if (i+1)%2==0:
                # go forward
                low = mid+1
            else:
                # go backward
                hi = mid -1
        return None