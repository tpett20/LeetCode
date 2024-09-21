# 539. Minimum Time Difference
# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for time in timePoints:
            hr, mins = time.split(":")
            flt = int(hr) + (int(mins) / 60)
            times.append(flt)
        times.sort()
        min_diff = float('inf')
        for i in range(1, len(times)):
            diff = times[i] - times[i - 1]
            min_diff = min(diff, min_diff)
        last_diff = (times[0] + 24) - times[-1]
        min_diff = min(last_diff, min_diff)
        return round(min_diff * 60)

s = Solution()
print(s.findMinDifference(["23:59", "00:00"]))
print(s.findMinDifference(["20:50", "00:53", "1:53"]))