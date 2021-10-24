class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        def p(arr):
            l=0
            s=0
            res=[]
            for i,v in enumerate(arr):
                if v=='*':
                    res.extend(['.']*(l-s)+['#']*s+['*'])
                    l=0
                    s=0
                    continue
                elif v=='#':
                    s+=1
                l+=1
            if l:
                res.extend(['.']*(l-s)+['#']*s)
            return res
        arr1 = [p(a) for a in box][::-1]
        return list(list(x) for x in zip(*arr1))