ff=lambda x,y:y+"."+x
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c=Counter()
        for i in cpdomains:
            i=i.split(" ")
            rep=int(i[0])
            for domain in accumulate(i[1].split(".")[::-1],ff):
                c[domain]+=rep
        return [ str(c[x])+" "+x for x in c]
    