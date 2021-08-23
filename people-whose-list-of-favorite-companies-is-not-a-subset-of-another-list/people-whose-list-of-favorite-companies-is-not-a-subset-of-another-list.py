class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        a=dict()
        for i,v in enumerate(favoriteCompanies):
            t=set(v)
            favoriteCompanies[i]=t
        ind=set()
        s=[]
        for i,v in enumerate(sorted(favoriteCompanies,reverse=True,key=len)):
            add=True
            for check in s:
                if v.issubset(check):
                    add=False
                    break
            if add:
                s.append(v)
                ind.add(favoriteCompanies.index(v))
        return sorted(ind)
                