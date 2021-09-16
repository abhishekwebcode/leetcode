class Node:
    def __init__(self):
        self.sum=0
        self.len=0
class UndergroundSystem:

    def __init__(self):
        self.stations=collections.defaultdict(Node)
        self.pending={}

    def checkIn(self, i: int, stationName: str, t: int) -> None:
        self.pending[i]=[stationName,t]

    def checkOut(self, i: int, stationName: str, t: int) -> None:
        [startStation,startTime]=self.pending[i]
        node=self.stations[(startStation,stationName)]
        node.sum+=t-startTime
        node.len+=1
        del self.pending[i]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        node=self.stations[(startStation,endStation)]
        return node.sum/node.len


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)