class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans=0
        for i in logs:
            if i==r"../":
                ans=max(ans-1,0)
            elif i==r"./":
                pass
            else:
                ans+=1
        return ans