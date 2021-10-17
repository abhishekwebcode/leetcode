class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split(' ')
        arr=[None for _ in range(len(words))]
        for j in words:
            arr[ int(j[-1])-1 ] = j[:-1]
        return " ".join(arr)
        