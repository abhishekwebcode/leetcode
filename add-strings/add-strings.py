class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans=[]
        l1 = len(num1)
        l2 = len(num2)
        if l1>l2:
            num2 = (l1-l2)*'0' + num2
        if l2>l1:
            num1 = (l2-l1)*'0' + num1
        num1=num1[::-1]
        num2=num2[::-1]
        carry=0
        for i in range(len(num1)):
            currentSum = int(num1[i])+int(num2[i])+carry
            ans.append(str(currentSum%10))
            carry = currentSum//10
        if carry:
            ans.append(str(carry))
        return "".join(ans[::-1])