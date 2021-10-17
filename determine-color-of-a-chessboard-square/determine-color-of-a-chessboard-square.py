class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a=['a','b','c','d','e','f','g','h']
        k=a.index(coordinates[0])+int(coordinates[1])
        return not k%2