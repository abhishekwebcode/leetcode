class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        class Item:
            __slots__=['index','val']
        ans = [0 for _ in range(len(temperatures))]
        st=[]
        for index in range(len(temperatures)):
            current  = temperatures[index]
            while st and st[-1].val<current:
                item = st.pop()
                ans[item.index]=index-item.index
            newitem = Item()
            newitem.val = current
            newitem.index = index
            st.append(newitem)
        return ans