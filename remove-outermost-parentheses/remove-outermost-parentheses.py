class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        temp=[]
        st=[]
        b=0
        for c in s:
            if c=='(':
                b+=1
            if c==')':
                b-=1
            st.append(c)
            if b==0:
                if st:
                    temp.append(st)
                st=[]
        ans=[]
        for arr in temp:
            arr.pop(0)
            arr.pop()
            ans.extend(arr)
        return "".join(ans)
            