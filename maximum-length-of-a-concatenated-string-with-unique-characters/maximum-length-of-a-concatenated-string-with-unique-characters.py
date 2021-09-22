class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr1=[]
        for a in arr:
            t=set(a)
            if len(a)==len(t):
                arr1.append(t)
        ans=0
        def rec(i,s):
            nonlocal ans
            if i==len(arr1):
                return
            currentSet=arr1[i]
            # take it
            if len(s.intersection(currentSet))==0:
                b=set()
                b.update(s)
                b.update(currentSet)
                ans=max(ans,len(b))
                rec(i+1,b)
            # skip it
            rec(i+1,s)
        rec(0,set())
        return ans