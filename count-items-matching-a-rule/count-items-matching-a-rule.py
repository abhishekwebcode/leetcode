class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans=0
        for t,c,n in items:
            if ruleKey=='type' and ruleValue==t:
                ans+=1
            if ruleKey=='color' and ruleValue==c:
                ans+=1
            if ruleKey=='name' and ruleValue==n:
                ans+=1
        return ans