class Solution:
    def getOdds(self,nums):
        indices=[]
        for i in range(len(nums)):
            if nums[i]%2!=0:
                indices.append(i)
                nums[i]-=1
        return indices
    def halfIt(self,nums):
        for i in range(len(nums)):
            nums[i]/=2
    def minOperations(self, nums: List[int]) -> int:
        ans=0
        while sum(nums)!=0:
            oddIndices=self.getOdds(nums)
            if oddIndices:
                ans+=len(oddIndices)
            else:
                self.halfIt(nums)
                ans+=1
        return ans