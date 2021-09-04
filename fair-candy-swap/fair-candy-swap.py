"""
alive gives a to bob
bob gives b to alice
net gain to alice is b-a
net gain to bob is a-b
aliceMore  = a - b
"""

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSum=sum(aliceSizes)
        bobSum=sum(bobSizes)
        diff=bobSum-aliceSum
        md=diff/2
        alice=set(aliceSizes)
        bob=set(bobSizes)
        for a in alice:
            if a+md in bob:
                return [a,a+md]