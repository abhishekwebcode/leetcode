import itertools
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff = float('inf')
        for i in range(k,len(nums)+1):
            window=nums[i-k:i]
            diff = min(diff,abs(window[0]-window[-1]))
        return diff