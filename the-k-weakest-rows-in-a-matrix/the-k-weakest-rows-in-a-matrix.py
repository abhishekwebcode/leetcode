class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return ([ x for x,y in  ( list(sorted( ( [ [i,v] for i,v in enumerate(list(map(sum,mat))) ] ) , key = lambda j:j[1]  )) ) ])[:k]
        