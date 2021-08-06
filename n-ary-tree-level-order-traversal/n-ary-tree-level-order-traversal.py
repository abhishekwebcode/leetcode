"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import defaultdict as d
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root==None:
            return []
        ans = d(list)
        def process(node,level):
            ans[level].append(node)
        def bfs(node,level):
            process(node.val,level)
            for child in node.children:
                bfs(child,level+1)
        bfs(root,1)
        print(ans)
        return ans.values()