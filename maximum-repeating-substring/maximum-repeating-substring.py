class Solution:
    def maxRepeating(self, s: str, word: str) -> int:
        i=1
        while i*word in s:
            i+=1
        return i-1