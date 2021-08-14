class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        s=list(s)
        for c in t:
            if s[0]==c:
                del s[0]
            if len(s)==0:
                return True
        return len(s)==0