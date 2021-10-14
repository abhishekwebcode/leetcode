class Solution:
    def minOperations(self, s: str) -> int:
        zero=one=0
        for i,c in enumerate(s):
            zeroStarting = '0' if not i%2 else '1'
            oneStarting = '0' if i%2 else '1'
            if zeroStarting!=c:
                zero+=1
            if oneStarting!=c:
                one+=1
        return min(zero,one)
                
            