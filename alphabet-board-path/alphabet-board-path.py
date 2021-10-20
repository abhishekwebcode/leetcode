board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
def g(c):
    for i,row in enumerate(board):
        if c in row:
            return (i,row.index(c))
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        ans=[]
        a,b = 0,0
        for c in target:
            x,y = g(c)
            if y<b:
                ans.extend(['L']*(b-y))
            if x<a:
                ans.extend(['U']*(a-x))
            if a<x:
                ans.extend(['D']*(x-a))
            if y>b:
                ans.extend(['R']*(y-b))
            ans.append('!')
            a,b = x,y
        return "".join(ans)