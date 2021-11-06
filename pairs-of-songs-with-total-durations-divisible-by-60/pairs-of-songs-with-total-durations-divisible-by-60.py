class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = defaultdict(int)
        ans=0
        for n in time:
            ans+=remainders[(-n%60)]
            remainders[n%60]+=1
        return ans
            