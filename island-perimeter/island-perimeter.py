class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    l=0
                    r=0
                    t=0
                    b=0
                    # check for left
                    if j==0:
                        l=1
                    elif grid[i][j-1]==0:
                        l=1
                    # check for right
                    if j==len(grid[0])-1 or grid[i][j+1]!=1:
                        r=1
                    # check for top
                    if i==0 or grid[i-1][j]==0:
                        t=1
                    # check for bottom
                    if i==len(grid)-1 or grid[i+1][j]==0:
                        b=1
                    ans+=l+r+t+b
        return ans
                    