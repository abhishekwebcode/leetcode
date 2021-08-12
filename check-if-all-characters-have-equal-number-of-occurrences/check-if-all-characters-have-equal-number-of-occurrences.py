class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = collections.Counter(s)
        freqs = list(c.values())
        return len(set(freqs))<2