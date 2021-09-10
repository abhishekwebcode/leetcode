from copy import deepcopy
class Solution:
    def imageSmoother(self, c: List[List[int]]) -> List[List[int]]:
        def g(i,j):
            d=[]
            if i!=0:
                d.extend(c[i-1][max(j-1,0):j+2])
            d.extend(c[i][max(0,j-1):j+2])
            if i!=len(c)-1:
                d.extend(c[i+1][max(0,j-1):j+2])
            return int(mean(d))
        matrix=deepcopy(c)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]=g(i,j)
        return matrix