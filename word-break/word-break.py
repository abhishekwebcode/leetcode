class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m=defaultdict(list)
        for word in wordDict:
            m[word[0]].append(word)
        for key in m:
            m[key].sort(reverse=True)
        @lru_cache(None)
        def rec(i):
            if i==len(s):
                return True
            possible = m[s[i]]
            if not possible:
                return False
            for word in possible:
                if len(s)-i>=len(word) and s[i:i+len(word)]==word:
                    if rec(i+len(word)):
                        return True
            return False
        return rec(0)