class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        class Person:
            __slots__=['tickets','index']
        t = []
        for i,ti in enumerate(tickets):
            temp = Person()
            temp.tickets = ti
            temp.index = i
            t.append(temp)
        d=t
        ans=0
        want = d[k]
        while want.tickets!=0:
            now = d.pop(0)
            if now.tickets:
                ans+=1
                now.tickets-=1
            d.append(now)
        return ans
            
                
                