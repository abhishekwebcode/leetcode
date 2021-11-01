class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        co=set()
        for i,riw in enumerate(board):
            for j,value in enumerate(riw):
                if value=='O':
                    co.add((i,j,))
        regions=defaultdict(set)
        def bfs(pos,s):
            s.add(pos)
            x,y = pos
            for dx,dy in [[0,-1],[-1,0],[1,0],[0,1]]:
                newx,newy = dx+x,dy+y
                if 0<=newx<len(board) and 0<=newy<len(board[0]) and  (newx,newy,) not in s and board[newx][newy]=='O':
                    bfs((newx,newy,),s)
            return s
        for pos in co.copy():
            if pos in co:
                cov=bfs(pos,set())
                regions[pos]=cov
                for j in cov:
                    co.remove(j)
        toCapture=set()
        def isS(area):
            for pos in area:
                x,y = pos
                if x==0 or x==len(board)-1 or y==0 or y==len(board[0])-1:
                    return False
                for dx,dy in [[0,-1],[-1,0],[1,0],[0,1]]:
                    newx,newy = dx+x,dy+y
                    if (newx,newy,) not in area and board[newx][newy]!='X':
                        return False
            return True
        for key in regions:
            area = regions[key]
            if isS(area):
                toCapture.add(key)
        for key in toCapture:
            for pos in regions[key]:
                x,y=pos
                board[x][y]='X'