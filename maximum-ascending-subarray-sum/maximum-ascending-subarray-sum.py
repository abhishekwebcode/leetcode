class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        m=nums[0]
        temp=nums[0]
        i=1
        while i<len(nums):
            if nums[i]>nums[i-1]:
                temp+=nums[i]
            else:
                m=max(m,temp)
                temp=nums[i]
            i+=1
        return max(m,temp)