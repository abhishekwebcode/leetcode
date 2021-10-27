class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a=[]
        self.min = float('inf')

    def push(self, val: int) -> None:
        if val<self.min:
            self.min=val
        self.a.append(val)
        

    def pop(self) -> None:
        if self.min==self.a.pop():
            if self.a:
                self.min = min(self.a)
            else:
                self.min=float('inf')

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()