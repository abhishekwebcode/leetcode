class Solution:
    def uniquePathsWithObstacles(self, o: List[List[int]]) -> int:
        if o[-1][-1]==1 or o[0][0]==1:
            return 0
        for i in range(len(o)):
            for j in range(len(o[0])):
                if o[i][j]==1:
                    o[i][j]=None
        for i in range(len(o)):
            if o[i][0] is not None:
                o[i][0]=1
            else:
                break
        for j in range(len(o[0])):
            if o[0][j] is not None:
                o[0][j]=1
            else:
                break
        for i in range(1,len(o)):
            for j in range(1,len(o[0])):
                if o[i][j]==0:
                    ans=0
                    if o[i-1][j] is not None and o[i-1][j]:
                        ans+=o[i-1][j]
                    if o[i][j-1] is not None and o[i][j-1]:
                        ans+=o[i][j-1]
                    o[i][j]=ans
        # ([print(x) for x in o])
        return o[-1][-1]
                    