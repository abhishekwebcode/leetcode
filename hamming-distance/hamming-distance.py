class Solution:
    def hammingDistance(self, x: int, y: int,ans:int=0) -> int:
        temp = x ^ y
        return bin(temp).count('1')