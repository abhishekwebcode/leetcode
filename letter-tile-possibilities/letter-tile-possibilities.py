class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans=0
        for i in range(1,len(tiles)+1):
            ans+=len( set(  list( itertools.permutations(tiles,i) ) ) )
        return ans