class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for turn in range(0,numRows):
            temp=[None]*(turn+1)
            temp[0]=temp[-1]=1
            if turn>1:
                prevRow = ans[-1]
                for index in range(1,len(temp)-1):
                    temp[index]=prevRow[index-1]+prevRow[index]
            ans.append(temp)
        return ans