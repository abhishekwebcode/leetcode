class Solution:
    def evaluate(self, s: str, k: List[List[str]]) -> str:
        k=dict(k)
        s=s.split('(')
        ans=[]
        for i in s:
            if not i:
                continue
            oo = i.split(')')
            if len(oo)==1:
                ans.extend(oo)
                continue
            oo[0] = k.get(oo[0],'?')
            ans.extend(oo)
        return ''.join(ans)