class Solution:
    def isThree(self, n: int) -> bool:
        if n==1 or n==2:
            return False
        gotOne=False
        for div in range(2,n):
            if n%div==0:
                if gotOne:
                    return False
                gotOne = True
        return gotOne