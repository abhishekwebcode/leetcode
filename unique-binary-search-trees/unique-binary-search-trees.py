class Solution:
    def numTrees(self, n: int) -> int:
        f=factorial(n)
        return factorial(2*n)//f//f//(n+1)

