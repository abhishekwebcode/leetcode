class Solution:
    def maxTurbulenceSize(self, nums: List[int]) -> int:
        l=len(nums)
        if l==1:
            return 1
        if l==2:
            if nums[0]==nums[1]:
                return 1
            return 2
        i=0
        ans=1
        while i<len(nums)-1:
            elementsLeft=l-1-i
            if ans>elementsLeft:
                break
            c=1
            if nums[i]==nums[i+1]:
                i+=1
                continue
            c+=1
            sign = nums[i]<nums[i+1]
            j=None
            for j in range(i+1,len(nums)-1):
                if nums[j]==nums[j+1]:
                    break
                newSign = nums[j]<nums[j+1]
                if sign==newSign:
                    break
                sign=newSign
                c+=1
            ans=max(ans,c)
            i+=1
        return ans