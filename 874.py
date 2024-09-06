# 874. Walking Robot Simulation
# A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:
    # -2: Turn left 90 degrees.
    # -1: Turn right 90 degrees.
    # 1 <= k <= 9: Move forward k units, one unit at a time.
# Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.
# Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).
# Note:
    # North means +Y direction.
    # East means +X direction.
    # South means -Y direction.
    # West means -X direction.
    # There can be obstacle in [0,0].

from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set()
        for obstacle in obstacles:
            x, y = obstacle
            obs.add((x, y))
        pos = [0, 0]
        max_dist = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        for command in commands:
            if command == -2:
                direction += 3
            elif command == -1:
                direction += 1
            else:
                step = dirs[direction % 4]
                for _ in range(command):
                    next = (pos[0] + step[0], pos[1] + step[1])
                    if next in obs:
                        break
                    pos = next
                dist = abs(pos[0]) ** 2 + abs(pos[1]) ** 2
                max_dist = max(dist, max_dist)
        return max_dist

s = Solution()
print(s.robotSim([4,-1,4,-2,4], [[2,4]]))