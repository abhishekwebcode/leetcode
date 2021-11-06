from collections import deque as q
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=set()
        rotten=set()
        empty = set()
        queue = []
        for i,row in enumerate(grid):
            for j,value in enumerate(row):
                if value == 0:
                    empty.add((i,j,))
                elif value==1:
                    fresh.add((i,j,))
                else:
                    rotten.add((i,j,))
                    queue.append((i,j,))
        if not fresh:
            return 0
        visited = set()
        m=0
        def gn(x,y):
            nonlocal visited,fresh
            neighbours=[]
            for dx,dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                pos = (x+dx,y+dy,)
                if pos not in visited and pos in fresh:
                    neighbours.append(pos)
            return neighbours
        while queue:
            m+=1
            temp=[]
            for x,y in queue:
                nn = gn(x,y)
                for pos in nn:
                    fresh.remove(pos)
                temp.extend(nn)
            queue=temp
        if fresh:
            return -1
        return m-1