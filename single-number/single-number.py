class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums=Counter(nums)
        for t in nums:
            if nums[t]==1:
                return t