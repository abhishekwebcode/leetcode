class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        pending=set(range(n))
        pending.remove(headID)
        subordinates=collections.defaultdict(list)
        for employeeId,managerId in enumerate(manager):
            if managerId!=-1:
                subordinates[managerId].append(employeeId)
        def dfs(i):
            cands=[]
            for subordinate in subordinates[i]:
                cands.append(dfs(subordinate))
            if not cands:
                return 0
            return informTime[i]+max(cands)
        return dfs(headID)