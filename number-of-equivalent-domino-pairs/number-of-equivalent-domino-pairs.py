class Solution:
    def numEquivDominoPairs(self, d: List[List[int]]) -> int:
        for i,v in enumerate(d):
            d[i]=tuple(sorted(d[i]))
        t=defaultdict(int)
        for i,v in enumerate(d):
            t[v]+=1
        del d
        return int(sum( [ ((x-1)*(x))/2 if x>1 else 0 for x in t.values() ] ))
        