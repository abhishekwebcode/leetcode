class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] is not 1:
            return False
        valueIndex=dict()
        for i,v in enumerate(stones):
            valueIndex[v]=i
        @lru_cache(None)
        def rec(i,k):
            nonlocal stones,valueIndex
            if i>=len(stones):
                return False
            if i==len(stones)-1:
                return True
            jump1value = stones[i]+(k-1)
            jump2value = stones[i]+(k)
            jump3value = stones[i]+(k+1)
            if jump3value in valueIndex and valueIndex[jump3value]>i:
                if rec(valueIndex[jump3value],k+1):
                    return True
            if jump2value in valueIndex and valueIndex[jump2value]>i:
                if rec(valueIndex[jump2value],k):
                    return True
            if jump1value in valueIndex and valueIndex[jump1value]>i:
                if rec(valueIndex[jump1value],k-1):
                    return True
            return False
        return rec(1,1)