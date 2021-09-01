class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        cycle = set()
        maxLength=-1
        def findLoop(index,encountered):
            if index in encountered:
                return
            encountered.add(index)
            return findLoop(nums[index],encountered)
        for index in range(len(nums)):
            if nums[index]==index:
                cycle.add(index)
                maxLength=max(maxLength,1)
            else:
                if index not in cycle:
                    encountered=set([index])
                    findLoop(nums[index],encountered)
                    for n in encountered:
                        cycle.add(n)
                    maxLength=max(maxLength,len(encountered))
        return maxLength