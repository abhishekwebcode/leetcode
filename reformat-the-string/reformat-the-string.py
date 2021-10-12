class Solution:
    def reformat(self, s: str) -> str:
        n=[]
        l=[]
        for c in s:
            if c.isdigit():
                n.append(c)
            else:
                l.append(c)
        if abs(len(n)-len(l))>1:
            return ""
        outer,inner=None,None
        if len(n)>len(l):
            outer = n
            inner=l
        else:
            outer = l
            inner=n
        e=[]
        def a1(i):
            nonlocal e
            if i is not None:
                e.append(i)
        for a,b in itertools.zip_longest(outer,inner):
            a1(a)
            a1(b)
        return "".join(e)