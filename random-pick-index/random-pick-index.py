from random import randrange
class Solution:

    def __init__(self, nums: List[int]):
        self.d=defaultdict(list)
        for i,v in enumerate(nums):
            self.d[v].append(i)

    def pick(self, target: int) -> int:
        arr=self.d[target]
        return arr[randrange(0,len(arr))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)