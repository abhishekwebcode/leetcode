# 1 3 5 7 , 400 
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        ans=0
        dp=[0]*len(str(n))+[1]
        for i in range(len(str(n))-1,-1,-1):
            for d in digits:
                if d<str(n)[i]:
                    dp[i]+= len(digits)**(len(str(n))-i-1)
                elif d==str(n)[i]:
                    dp[i]+= dp[i+1]
        return dp[0]+sum([ pow(len(digits),k) for k in range(1,len(str(n))) ])