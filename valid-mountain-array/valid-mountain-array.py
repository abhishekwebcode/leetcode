class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        ds=False
        ei=False
        ed=False
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                return False
            if ds==False:
                if arr[i]>arr[i-1]:
                    ei=True
                    continue
                if arr[i]<arr[i-1]:
                    ed=True
                    ds=True
            else:
                if arr[i]<arr[i-1]:
                    continue
                if arr[i]>arr[i-1]:
                    return False
        return ei and ed
                
                