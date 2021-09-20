class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        a = [ [ "" for x in range(3) ] for j in range(3) ]
        turn="A"
        for x,y in moves:
            a[x][y]=turn
            turn = "A" if turn=="B" else "B"
        # check diagonals
        if a[0][0]==a[1][1]==a[2][2] and a[0][0]!="":
            return a[0][0]
        if a[0][2]==a[1][1]==a[2][0] and a[2][0]!="":
            return a[2][0]
        # check rows
        for row in range(3):
            if a[row][0]==a[row][1]==a[row][2] and a[row][0]!="":
                return a[row][0]
        # check columns
        for col in range(3):
            if a[0][col]==a[1][col]==a[2][col] and a[0][col]!="":
                return a[0][col]
        if len(moves)==9:
            return "Draw"
        return "Pending"