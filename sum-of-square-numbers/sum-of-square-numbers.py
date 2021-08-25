class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        root=math.sqrt(c)
        if int(root)==root:
            return True
        for i in range(1,int(root)+1):
            left = math.sqrt(c-i**2)
            if left==int(left):
                return True
        return False