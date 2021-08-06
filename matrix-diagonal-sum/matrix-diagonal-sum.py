class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primarySum =  sum(mat[i][j] if i==j else 0 for i in range(0,len(mat)) for j in range(0,len(mat)) )
        seconday =  sum(mat[i][j] if i+j==len(mat)-1 else 0 for i in range(0,len(mat)) for j in range(0,len(mat)) )
        mid = None if len(mat)%2==0 else int( (len(mat)-1)/2 )
        a=mat[mid][mid] if (mid is not None) else 0
        print(primarySum,seconday,mid,a)
        return primarySum + seconday - a