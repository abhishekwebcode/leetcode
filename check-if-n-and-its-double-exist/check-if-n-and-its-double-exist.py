class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        c=set()
        for i,v in enumerate(arr):
            if 2*v in c or (v%2==0 and v/2 in c):
                return True
            c.add(v)
        return False