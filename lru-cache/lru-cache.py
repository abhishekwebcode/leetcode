class LRUCache:

    def __init__(self, capacity: int):
        self.a=dict()
        self.c=capacity
        self.keyused=[]

    def get(self, key: int) -> int:
        # print("GET: key=>",key)
        # print("GET BEFORE",self.keyused)
        if key in self.a:
            ind=self.keyused.index(key)
            self.keyused.pop(ind)
            self.keyused.append(key)
            """print("GET AFTER",self.keyused)
            print()"""
            return self.a[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # print("PUT BEFORE: key",key,"keyused",self.keyused)
        if key not in self.keyused:
            self.keyused.append(key)
        else:
            ind=self.keyused.index(key)
            self.keyused.pop(ind)
            self.keyused.append(key)
        self.a[key]=value
        if len(self.keyused)>self.c:
            discard=self.keyused.pop(0)
            del self.a[discard]
        # print("PUT AFTER: key",key,"keyused",self.keyused)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)