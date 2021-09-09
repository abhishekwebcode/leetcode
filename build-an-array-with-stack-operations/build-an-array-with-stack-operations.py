class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target=set(target)
        ans=[]
        elemAdded=0
        for i in range(1,n+1):
            ans.append('Push')
            if i not in target:
                ans.append('Pop')
            else:
                elemAdded+=1
            if elemAdded==len(target):
                return ans
        return ans
                
            