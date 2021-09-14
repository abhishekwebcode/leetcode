a=ord('a')
charset=set([chr(a+i) for i in range(26)])
class Solution:
    def modifyString(self, s: str) -> str:
        if len(s)==1:
            if s=="?":
                return "a"
        s=list(s)
        if s[0]=="?":
            s[0] = list(charset-set([s[1]]))[0]
        for i in range(1,len(s)-1):
            if s[i]=="?":
                s[i] = list(charset-set([s[i-1],s[i+1]]))[0]
        if s[-1]=="?":
            s[-1] = list(charset-set([s[-2]]))[0]
        return "".join(s)