class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<3:
            return s
        temp = s[:2]
        for i in range(2,len(s)):
            if s[i] is not s[i-1] or s[i] is not s[i-2]:
                temp+=s[i]
        return temp