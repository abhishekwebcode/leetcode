class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([ True if len(str(x))%2==0 else False for x in nums ])