# 57. Insert Interval
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        
        output = []
        i = 0
        while newInterval[0] > intervals[i][1]:
            output.append(intervals[i])
            i += 1
        if newInterval[1] < intervals[i][0]:
            output.append(newInterval)
        else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            while i < len(intervals) and newInterval[1] > intervals[i][1]:
                i += 1
            if i < len(intervals) and newInterval[1] >= intervals[i][0] and newInterval[1] <= intervals[i][1]:
                newInterval[1] = intervals[i][1]
                i += 1
            output.append(newInterval)
        while i < len(intervals):
            output.append(intervals[i])
            i += 1
        return output

s = Solution()
print(s.insert([[1,3],[6,9]], [2,5]))
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(s.insert([[1,2],[3,5],[6,7],[9,10],[12,16]], [4,8]))
print(s.insert([[1,2],[3,5],[6,7],[9,10],[12,16]], [8,8]))
print(s.insert([[1,5]], [2,3]))
print(s.insert([[1,5],[6,8]], [3,7]))