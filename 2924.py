# 2924. Find Champion II
# There are n teams numbered from 0 to n - 1 in a tournament; each team is also a node in a DAG.
# You are given the integer n and a 0-indexed 2D integer array edges of length m representing the DAG, where edges[i] = [ui, vi] indicates that there is a directed edge from team ui to team vi in the graph.
# A directed edge from a to b in the graph means that team a is stronger than team b and team b is weaker than team a.
# Team a will be the champion of the tournament if there is no team b that is stronger than team a.
# Return the team that will be the champion of the tournament if there is a unique champion, otherwise, return -1.
# Notes
    # A cycle is a series of nodes a1, a2, ..., an, an+1 such that node a1 is the same node as node an+1, the nodes a1, a2, ..., an are distinct, and there is a directed edge from the node ai to node ai+1 for every i in the range [1, n].
    # A DAG is a directed graph that does not have any cycle.

from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0
        strength = {}
        for edge in edges:
            strong, weak = edge
            strength[weak] = False
            if strong not in strength:
                strength[strong] = True
        if len(strength) != n:
            return -1
        champs = []
        for player in strength:
            if strength[player]:
                champs.append(player)
        return champs[0] if len(champs) == 1 else -1
    
s = Solution()
print(s.findChampion(3, [[0,1],[1,2]]))
print(s.findChampion(4, [[0,2],[1,3],[1,2]]))
print(s.findChampion(1, []))