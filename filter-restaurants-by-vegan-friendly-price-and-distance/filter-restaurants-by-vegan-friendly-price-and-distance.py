class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        f=defaultdict(list)
        for id1,rating,vegan,price,distance in restaurants:
            if veganFriendly and not vegan:
                continue
            if price>maxPrice or distance>maxDistance:
                continue
            f[rating].append(id1)
        del restaurants
        g=dict()
        for t in f:
            y=f[t]
            y.sort(reverse=True)
            g[t]=y
        del f
        ans=[]
        for key in sorted(g.keys(),reverse=True):
            ans.extend(g[key])
        return ans
            