class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i and j:
                    grid[i][j]+=min(grid[i][j-1],grid[i-1][j])
                else:
                    if i:
                        grid[i][j]+=grid[i-1][j]
                    if j:
                        grid[i][j]+=grid[i][j-1]
        return grid[-1][-1]