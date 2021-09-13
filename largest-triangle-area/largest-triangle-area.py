class Solution:
    def largestTriangleArea(self, p: List[List[int]]) -> float:
        return max(0.5 * abs(xa*yb + xb*yc + xc*ya - xb*ya - xc*yb - xa*yc)
                   for (xa, ya), (xb, yb), (xc, yc) in itertools.combinations(p, 3))