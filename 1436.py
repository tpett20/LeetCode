# 1436. Destination City
# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        map = {}
        for path in paths:
            s = path[0]
            if s in map:
                del map[s]
            else:
                map[s] = 0
            d = path[1]
            if d in map:
                del map[d]
            else:
                map[d] = 1
        for city in map:
            if map[city] == 1:
                return city

s = Solution()
print(s.destCity([["London","New York"], ["New York","Lima"], ["Lima","Sao Paulo"]]))
print(s.destCity([["B","C"], ["D","B"], ["C","A"]]))
print(s.destCity([["A","Z"]]))