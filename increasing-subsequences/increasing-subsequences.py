class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        for i in range(len(nums)):
            temp=[]
            for j in range(i+1,len(nums)):
                if nums[j]>=nums[i]:
                    temp2=[]
                    for pair in temp:
                        if nums[j]>=pair[-1]:
                            temp2.append(pair[:]+[nums[j]])
                    temp.extend(temp2)
                    temp.append([nums[i],nums[j]])
            for pair in temp:
                ans.add(tuple(pair))
        return ans
            