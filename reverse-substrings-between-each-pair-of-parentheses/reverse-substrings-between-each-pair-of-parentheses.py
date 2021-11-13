class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        ans=[]
        def doPop():
            temp = []
            while st[-1]!='(':
                temp.append(st.pop()[::-1])
            st.pop()
            temp=temp
            return "".join(temp)
        for c in s:
            if c==')':
                st.append(doPop())
            else:
                st.append(c)
        return ''.join(st)