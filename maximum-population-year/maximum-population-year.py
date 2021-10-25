class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        c=defaultdict(int)
        ans=0
        m=0
        for s,e in logs:
            for i in range(s,e):
                c[i]+=1
                if c[i]>m:
                    m=c[i]
                    ans=i
                elif i<ans and c[i]==m:
                    ans=i
        return ans