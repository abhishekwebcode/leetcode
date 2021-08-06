class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            try:
                nums.remove(val)
            except Exception as e:
                break
        return len(nums)