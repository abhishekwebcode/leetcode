class Solution:
    def countBalls(self, l: int, h: int) -> int:
        d=defaultdict(int)
        def s(n):
            s=0
            while n:
                n,r=divmod(n,10)
                s+=r
            return s
        m=float('-inf')
        for i in range(l,h+1):
            su=s(i)
            d[su]+=1
            m=max(m,d[su])
        return m
        return sum(True for key in d if d[key]==m)
        