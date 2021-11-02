class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        sx,sy=None,None
        ex,ey =None,None
        noWalk = set()
        m,n = len(grid),len(grid[0])
        walk = 0
        def canWalk(i,j,visited):
            nonlocal m,n
            if not (0<=i<m) or not(0<=j<n):
                return False
            pos = (i,j,)
            if pos in visited:
                return False
            if pos in noWalk:
                return False
            return True
        def backtrack(x,y,visited):
            nonlocal canWalk,noWalk,ex,ey
            if x==ex and y==ey:
                return 1 if len(visited)==walk else 0
            ans=[0]
            for dx,dy in [[0,1],[0,-1],[-1,0],[1,0]]:
                newx,newy = x+dx,y+dy
                if canWalk(newx,newy,visited):
                    ss = visited.copy()
                    ss.add((newx,newy,))
                    ans.append(backtrack(newx,newy,ss))
            return sum(ans)
        for i,row in enumerate(grid):
            for j,value in enumerate(row):
                if value == 1:
                    walk+=1
                    sx,sy = i,j,
                elif value == 2:
                    walk+=1
                    ex,ey = i,j,
                elif value==-1:
                    noWalk.add((i,j,))
                else:
                    walk+=1
        ss=set()
        if not canWalk(sx,sy,ss):
            return 0
        ss.add((sx,sy,))
        return backtrack(sx,sy,ss)