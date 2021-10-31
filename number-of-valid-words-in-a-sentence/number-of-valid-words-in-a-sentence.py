import string
allowed = set()
for s in [string.ascii_lowercase,['-','!','.',',']]:
    allowed.update(s)

def isValid(temp):
    if all(c in allowed for c in temp):
        if temp.count('-')<2 and temp.count('!')+temp.count('.')+temp.count(',')<2:
            for i,c in enumerate(temp):
                if c=='-':
                    if i==0 or i==len(temp)-1 or not temp[i-1].islower() or not temp[i+1].islower():
                        return False
                if c in ['!','.',','] and i!=len(temp)-1:
                    return False
            return True
class Solution:
    def countValidWords(self, sentence: str) -> int:
        ans=0
        temp=[]
        for c in sentence:
            if c!=' ':
                temp.append(c)
            else:
                if temp:
                    if isValid(temp):
                        ans+=1
                    temp=[]
        if temp:
            if isValid(temp):
                ans+=1
        return ans