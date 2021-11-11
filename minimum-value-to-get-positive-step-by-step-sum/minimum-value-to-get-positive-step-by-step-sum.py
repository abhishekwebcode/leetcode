class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n=min(list(itertools.accumulate(nums,lambda x,y:x+y)))
        if n<0:
            return abs(n)+1
        return 1
        