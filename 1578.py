# 1578. Minimum Time to Make Rope Colorful
# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.
# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
# Return the minimum time Bob needs to make the rope colorful.

class Solution:
    def minCost(self, colors: str, needed_time: list[int]) -> int:
        min_time = 0
        i = 1
        while i < len(colors):
            if colors[i] == colors[i - 1]:
                sum = needed_time[i - 1]
                max_time = needed_time[i - 1]
                while i < len(colors) and colors[i] == colors[i - 1]:
                    max_time = max(needed_time[i], max_time)
                    sum += needed_time[i]
                    i += 1
                sum -= max_time
                min_time += sum
            i += 1
        return min_time
            

s = Solution()
print(s.minCost("abaac", [1,2,3,4,5]))
print(s.minCost("abc", [1,2,3]))
print(s.minCost("aabaa", [1,2,3,4,1]))