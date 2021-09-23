class Solution:
    def breakPalindrome(self, p: str) -> str:
        l=len(p)
        if l==1:
            return ""
        for i in range(len(p)):
            if l%2 and i==((l//2)+1):
                continue
            if ord(p[i])>ord('a'):
                ans=p[:i]+'a'+p[i+1:]
                if ans!=ans[::-1]:
                    return ans
        return p[:-1]+'b'
        
                