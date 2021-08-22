class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack=[homepage]
        self.i=0

    def visit(self, url: str) -> None:
        self.stack=self.stack[:self.i+1]
        self.stack.append(url)
        self.i+=1
        print("VISIT",self.stack,self.i,url)

    def back(self, steps: int) -> str:
        print("BACKSTART",self.i,steps,self.stack)
        back=min(steps,self.i)
        self.i-=back
        return self.stack[self.i]
            

    def forward(self, steps: int) -> str:
        forward = min(len(self.stack)-1-self.i,steps)
        self.i+=forward
        return self.stack[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)