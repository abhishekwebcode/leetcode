class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @functools.lru_cache(None)
        def rec(ind):
            nonlocal nums
            if ind>=len(nums):
                return False
            if ind==len(nums)-1:
                return True
            for jump in range(nums[ind],0,-1):
                if rec(ind+jump):
                    return True
            return False
        return rec(0)