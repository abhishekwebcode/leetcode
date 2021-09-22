class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        temp=0
        for v in nums:
            if v==1:
                temp+=1
            else:
                ans=max(ans,temp)
                temp=0
        return max(ans,temp)
        