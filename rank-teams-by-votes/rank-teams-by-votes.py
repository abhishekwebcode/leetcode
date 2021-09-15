class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        d = {}
        for vote in votes:
            for i, char in enumerate(vote):
                if char not in d:
                    d[char] = [0] * len(vote)
                d[char][i] += 1
        
        return "".join(sorted(d.keys(), key=lambda x: (d[x],65-ord(x)), reverse=True))