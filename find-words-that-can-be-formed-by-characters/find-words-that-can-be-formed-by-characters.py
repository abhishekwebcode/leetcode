class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c=0
        cnt=Counter(chars)
        for w in words:
            if len(Counter(w)-cnt)==0:
                c+=len(w)
        return c