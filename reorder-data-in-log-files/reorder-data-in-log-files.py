class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        d=[]
        l=[]
        for log in logs:
            a=log.split(" ")
            if a[1][0].isdigit():
                d.append(log)
            else:
                l.append(tuple( [ a[0], " ".join(a[1:]) ] ) )
        l=sorted(l,key=lambda x:(x[1],x[0]))
        l=[ x+" "+y for x,y in l]
        return l+d