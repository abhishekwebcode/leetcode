import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x!=abs(x):
            return False
        num = x
        intarr=[]
        while num>0:
            lastdigit = num % 10
            num = num // 10
            intarr.append(lastdigit)
        palinDrome = 0
        print(intarr)
        for index,value in enumerate(intarr):
            palinDrome+=value*math.pow(10,len(intarr)-1-index)
        print(palinDrome)
        return palinDrome==x