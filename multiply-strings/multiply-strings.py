"""
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        def sumLists(l):
            carry=0
            ans=[]
            for col in range(len(l[0])-1,-1,-1):
                t=carry
                for row in l:
                    t+=int(row[col])
                ans.insert(0,str(t%10))
                carry=t//10
            return ans
        def mul(step,num1,d):
            if d=="0":
                return None
            a=[]
            i=-1
            carry=0
            for i in range(len(num1)-1,-1,-1):
                r = int(num1[i])*d+carry
                a.insert(0,str(r%10))
                carry=r//10
                i-=1
            a.insert(0,str(carry))
            a.extend(["0"]*step)
            return a
        temp=[]
        maxL=0
        for i in range(len(num2)-1,-1,-1):
            if num2[i]=="0":
                continue
            interM=mul(len(num2)-1-i,num1,int(num2[i]))
            temp.append( interM )
            maxL=max(len(interM),maxL)
        temp1=[]
        for t in temp:
            init=["0"]*(maxL-len(t))
            init.extend(t)
            temp1.append(init)
        ans=sumLists(temp1)
        i=0
        while ans[i]=="0":
            i+=1
        return "".join(ans[i:])
        