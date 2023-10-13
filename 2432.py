# 2432. The Employee That Worked on the Longest Task
# There are n employees, each with a unique id from 0 to n - 1.
# You are given a 2D integer array logs where logs[i] = [idi, leaveTimei] where:
# - idi is the id of the employee that worked on the ith task, and
# - leaveTimei is the time at which the employee finished the ith task. All the values leaveTimei are unique.
# Note that the ith task starts the moment right after the (i - 1)th task ends, and the 0th task starts at time 0.
# Return the id of the employee that worked the task with the longest time. If there is a tie between two or more employees, return the smallest id among them.

class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        lastHr = 0
        maxTime = 0
        maxId = -1
        for log in logs:
            time = log[1] - lastHr
            if time > maxTime or (time == maxTime and log[0] < maxId):
                maxTime = time
                maxId = log[0]
            lastHr = log[1]
        return maxId

s = Solution()
print(s.hardestWorker(10, [[0,3],[2,5],[0,9],[1,15]]))
print(s.hardestWorker(2, [[0,10],[1,20]]))
print(s.hardestWorker(70, [[36,3],[1,5],[12,8],[25,9],[53,11],[29,12],[52,14]]))