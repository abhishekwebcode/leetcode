class Solution:
    def getPart(self,num):
        [r,i]=num.split('+')
        i=i.split('i')[0]
        return [int(r),int(i)]
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        [r1,i1]=self.getPart(num1)
        [r2,i2]=self.getPart(num2)
        r=(r1*r2)+(i1*i2*-1)
        i=(r1*i2)+(r2*i1)
        return str(r)+"+"+str(i)+"i"