class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0]*len(code)
        temp=code
        c=code*3
        ans=[]
        print(c)
        for i in range(len(temp)):
            if k>0:
                ans.append(sum(c[i+1:i+k+1]))
            else:
                #[2, 4, 9, 3, 2, 4, 9, 3, 2, 4, 9, 3]
                print(c[len(code)+i+k:len(code)+i])
                ans.append(sum( c[len(code)+i+k:len(code)+i]  ))
        return ans
            