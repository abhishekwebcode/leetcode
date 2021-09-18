class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        if not s1:
            return s2==s3
        if not s2:
            return s1==s3
        if len(s1)==1 or len(s2)==1:
            return s1+s2==s3 or s2+s1==s3
        @functools.lru_cache(None)
        def rec(i,j,k):
            """if i==len(s1) and j==0:
                return False
            if j==len(s2) and i==0:
                return False"""
            if k==len(s3):
                return True
            if i<len(s1):
                if s3[k]==s1[i]:
                    if rec(i+1,j,k+1):
                        return True
            if j<len(s2):
                if s3[k]==s2[j]:
                    if rec(i,j+1,k+1):
                        return True
            return False
        return rec(0,0,0)