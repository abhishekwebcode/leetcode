class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ls=collections.defaultdict(set)
        self.d=dict()


    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.d:
            freq = self.d[key]
            self.ls[freq].remove(key)
            if len(self.ls[freq])==0:
                del self.ls[freq]
            self.d[key]+=1
            self.ls[freq+1].add(key)
        else:
            self.ls[1].add(key)
            self.d[key]=1
        

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if self.d[key]==1:
            self.ls[1].remove(key)
            if len(self.ls[1])==0:
                del self.ls[1]
            del self.d[key]
        else:
            freq=self.d[key]
            self.ls[freq].remove(key)
            self.ls[freq-1].add(key)
            self.d[key]-=1
            if len(self.ls[freq])==0:
                del self.ls[freq]

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        keys  = self.ls.keys()
        if len(keys)>0:
            m = max(keys)
            s= self.ls[m]
            if len(s)>0:
                return next(iter(s),"")
        return ""
        
    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        keys  = self.ls.keys()
        if len(keys)>0:
            m = min(keys)
            s= self.ls[m]
            if len(s)>0:
                return next(iter(s),"")
        return ""

        
        
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()