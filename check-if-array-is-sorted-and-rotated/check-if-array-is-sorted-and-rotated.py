class Solution:
    def check(self, a: List[int]) -> bool:
        c=0
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                c+=1
        if a[-1]>a[0]:
            c+=1
        return c<=1