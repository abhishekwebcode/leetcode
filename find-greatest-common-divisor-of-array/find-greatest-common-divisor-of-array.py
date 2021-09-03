class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s,l=min(nums),max(nums)
        return max([ i if s%i==0 and l%i==0 else False for i in range(1,(s)+1) ])
            