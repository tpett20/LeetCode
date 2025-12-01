# 797. All Paths From Source to Target
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

from typing import List

class Solution:
    def __init__(self):
        self.all_paths = []
        self.n = 0

    def dfs(self, idx: int, path: List[int], graph: List[List[int]]) -> None:
        c_path = path.copy()
        c_path.append(idx)
        options = graph[idx]
        if idx == self.n - 1:
            self.all_paths.append(c_path)
        for option in options:
            self.dfs(option, c_path, graph)
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.n = len(graph)
        self.dfs(0, [], graph)
        return self.all_paths

s = Solution()
print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))
print(s.allPathsSourceTarget([[4,3,1],[3,2,4],[],[4],[]]))