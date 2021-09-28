class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m=[list(accumulate(row,lambda x,y:x+y)) for row in matrix]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=0
        for row in range(row1,row2+1):
            temp= self.m[row][col2]- ( self.m[row][col1-1] if col1!=0 else 0 )
            ans+=temp
        return ans

    

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)