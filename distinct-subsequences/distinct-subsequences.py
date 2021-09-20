class Solution:
    def numDistinct(self, st: str, t: str) -> int:
        @lru_cache(None)
        def rec(i,s):
            nonlocal t
            ans=0
            if len(s)>len(t):
                return 0
            if s==t:
                return 1
            if i>=len(st):
                return 0
            if t[len(s)]==st[i]:
                # take i 
                ans+=rec(i+1,s+st[i])
            # dont take i
            ans+=rec(i+1,s)
            return ans
        return rec(0,"")