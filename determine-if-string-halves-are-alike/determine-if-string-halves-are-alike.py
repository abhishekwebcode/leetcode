class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v=set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        l=len(s)//2
        a,b=s[:l],s[l:]
        def getV(s,v):
            return sum(True for c in s if c in v)
        return getV(a,v)==getV(b,v)
            