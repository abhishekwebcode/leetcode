class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        l1= "".join(([x if x.isdigit() else ' ' for x in word])).split(" ")
        a=set()
        for t in l1:
            if t.isdigit():
                a.add(int(t))
        return len(a)