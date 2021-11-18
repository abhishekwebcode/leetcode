class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            c=abs(nums[i])
            nums[c-1]=-1*abs(nums[c-1])
        return list(i+1 for i in range(len(nums)) if nums[i]>0)