class Solution:
    def reverseWords(self, s: str) -> str:
        ans=[]
        for w in s.split(' '):
            if not w.strip():
                ans.append(w)
            else:
                ans.append(w[::-1])
        return ' '.join(ans)