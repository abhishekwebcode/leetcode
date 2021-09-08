class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        inds=[]
        for i in range(len(nums)):
            if nums[i]==target:
                inds.append(i)
        ind=bisect.bisect_left(inds,start)
        arr=inds[max(0,ind-1):ind+1]
        ans=len(nums)
        for elem in arr:
            ans=min(ans,abs(elem-start))
        return ans