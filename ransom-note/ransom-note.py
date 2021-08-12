class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c=collections.Counter(magazine)
        for t in ransomNote:
            if c[t]>0:
                c[t]-=1
                continue
            return False
        return True