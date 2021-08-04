class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for a in nums:
            if a in s:
                return True
            s.add(a)
        return False