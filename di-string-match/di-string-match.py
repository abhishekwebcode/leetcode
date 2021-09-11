class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i=0
        j=len(s)
        ans=[]
        for c in s:
            if c=='D':
                ans.append(j)
                j-=1
            else:
                ans.append(i)
                i+=1
        return ans+[j]
                    