class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i in range(len(nums)):
            num = nums[i]
            want = target - num
            if want in a:
                return [i,a[want]]
            a[num]=i