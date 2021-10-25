class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lengths = [len(x) for x in words]
        words = [set(x) for x in words]
        ans=0
        checked = set()
        for i,seta in enumerate(words):
            for j,setb in enumerate(words):
                if (i,j,) in checked:
                    continue
                checked.add((j,i,))
                if i!=j:
                    if not seta.intersection(setb):
                        ans=max(ans,lengths[i]*lengths[j])
        return ans