class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        inds=[]
        chars=[]
        for i,c in enumerate(s):
            if c.isalpha():
                inds.append(i)
                chars.append(c)
        chars.reverse()
        for i,v in enumerate(inds):
            s[v]=chars[i]
        return "".join(s)