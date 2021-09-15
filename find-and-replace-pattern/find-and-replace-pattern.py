class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans=[]
        for word in words:
            d={}
            rd={}
            i=0
            while i<len(word):
                char=word[i]
                patternIndex = i%len(pattern)
                patternChar=pattern[patternIndex]
                if patternChar in d:
                    if char!=d[patternChar]:
                        break
                else:
                    if char in rd and rd[char]!=patternChar:
                        break
                    d[patternChar]=char
                    rd[char]=patternChar
                i+=1
            if i==len(word):
                ans.append(word)
        return ans