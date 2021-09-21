class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def rec(i,j):
            nonlocal word1,word2
            if j==len(word2):
                return len(word1)-(i+1)
            if i==len(word1):
                return len(word2)-j-1
            if word1[i]==word2[j]:
                return rec(i+1,j+1)
            cands=[]
            # insert
            cands.append(1+rec(i,j+1))
            # delete
            cands.append(1+rec(i+1,j))
            # replace
            cands.append(1+rec(i+1,j+1))
            return min(cands)
        return 1+rec(0,0)