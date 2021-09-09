class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        i = set(list1).intersection(set(list2))
        list1=dict([ (v,i) for i,v in enumerate(list1)])
        list2=dict([(v,i) for i,v in enumerate(list2)])
        ans=[[],None]
        for a in i:
            if ans[1]==None:
                ans=[[a],list1[a]+list2[a]]
            else:
                if ans[1]==list1[a]+list2[a]:
                    ans[0].append(a)
                if ans[1]>list1[a]+list2[a]:
                    ans=[[a],list1[a]+list2[a]]
        return ans[0]
                