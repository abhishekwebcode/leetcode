class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def rec(i1,i2):
            if i1==len(s1):
                return len(s2)-i2
            if i2==len(s2):
                return len(s1)-i1
            if s1[i1]==s2[i2]:
                return rec(i1+1,i2+1)
            return 1+min(rec(i1+1,i2),rec(i1,i2+1))
        return rec(0,0)