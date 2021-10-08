class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        inds=defaultdict(list)
        for i,c in enumerate(s):
            inds[c].append(i)
        for pind in inds[goal[0]]:
            ending = s[pind:]
            if goal[:len(ending)]==ending:
                # check first half
                starting = s[:pind]
                if goal[len(ending):]==starting:
                    return True
        return False