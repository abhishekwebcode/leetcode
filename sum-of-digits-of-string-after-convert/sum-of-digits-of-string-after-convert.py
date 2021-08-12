class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = [str(ord(x)-ord('a')+1) for x in s]
        def transform(i):
            st=list("".join(i))
            su = sum([ int(x) for x in st  ])
            return list(str(su))
        for _ in range(k):
            print(s)
            s = transform(s)
            print([s])
        return int("".join(s))