[0,1,0]
[0,0,1]

1
1
1

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        a=((0,-1),(0,1),(-1,0),(1,0),)
        def pollute(ii,jj,oldColor,newColor,seen):
            nonlocal image,a
            seen.add((ii,jj,))
            for (dx,dy,) in a:
                i=dx+ii
                j=dy+jj
                if (i,j,) in seen or i<0 or i>=len(image) or j<0 or j>=len(image[0]):
                    continue
                if image[i][j]==oldColor:
                    pollute(i,j,oldColor,newColor,seen)
                    image[i][j]=newColor
        pollute(sr,sc,image[sr][sc],newColor,set())
        image[sr][sc]=newColor
        return image