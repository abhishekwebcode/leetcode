class Solution:
    def minCost(self, st: str, cost: List[int]) -> int:
        def process(s,e):
            arr=cost[s:e+1]
            return sum(arr)-max(arr)
        i=0
        last=None
        s,e=None,None
        ans=0
        while i<len(st):
            if st[i]==last:
                if s==None:
                    s=i-1
                e=i
            else:
                if s!=None and e!=None:
                    ans+=process(s,e)
                s,e=None,None
            last=st[i]
            i+=1
        if s!=None and e!=None:
            ans+=process(s,e)
        return ans