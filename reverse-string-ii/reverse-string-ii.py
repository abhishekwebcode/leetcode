class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a=[]
        for i in range(0,len(s),2*k):
            ss = s[i:i+2*k]
            f1 = ss[:k]
            s1 = ss[k:]
            a.append(f1[::-1])
            if s1:
                a.append(s1)
        return "".join(a)