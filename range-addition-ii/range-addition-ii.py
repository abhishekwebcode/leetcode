class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        xx = min(x[0] for x in ops)
        yy = min(y[1] for y in ops)
        return xx*yy