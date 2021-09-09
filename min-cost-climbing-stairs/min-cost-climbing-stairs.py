class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def dp(i):
            if i>=len(cost):
                return 0
            return cost[i]+min(dp(i+2),dp(i+1))
        return min(dp(1),dp(0))
    