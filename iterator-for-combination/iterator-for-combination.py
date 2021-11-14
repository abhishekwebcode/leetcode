class CombinationIterator:

    def __init__(self, s: str, l: int):
        self.s=s
        self.l=l
        import itertools
        self.it = itertools.combinations(s,l)
        self.next1 = next(self.it,False)
        
        
    def next(self) -> str:
        ret =  self.next1
        self.next1 = next(self.it,False)
        return "".join(ret)

    def hasNext(self) -> bool:
        return self.next1!=False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()