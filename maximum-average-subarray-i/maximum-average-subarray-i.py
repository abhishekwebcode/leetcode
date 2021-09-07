class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k==1:
            return max(nums)
        def mean(arr):
            nonlocal k
            return sum(arr)/k
        m = mean(nums[0:k])
        rm=m
        print(m)
        for i in range(k,len(nums)):
            j= rm + ( ( nums[i]-nums[i-k] ) / k )
            m=max(j,m)
            rm=j
        return m