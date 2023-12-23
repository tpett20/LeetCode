# 1496. Path Crossing
# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = (0, 0)
        visited = {pos}
        for step in path:
            if step == "W":
                pos = (pos[0] + 1, pos[1])
            elif step == "E":
                pos = (pos[0] - 1, pos[1])
            elif step == "N":
                pos = (pos[0], pos[1] + 1)
            else:
                pos = (pos[0], pos[1] - 1)
            if pos in visited: 
                return True
            else:
                visited.add(pos)
        return False
    
s = Solution()
print(s.isPathCrossing("NES"))
print(s.isPathCrossing("NESWW"))