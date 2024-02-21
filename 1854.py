# 1854. Maximum Population Year
# You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.
# The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.
# Return the earliest year with the maximum population.

class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        births = []
        deaths = []
        for log in logs:
            births.append(log[0])
            deaths.append(log[1])
        births.sort(reverse=True)
        deaths.sort(reverse=True)
        
        max_pop = popul = 1
        max_year = births.pop()
        while len(births):
            if births[-1] < deaths[-1]:
                popul += 1
                year = births.pop()
                if popul > max_pop:
                    max_year = year
                    max_pop = popul
            else:
                deaths.pop()
                popul -= 1
        return max_year

s = Solution()
print(s.maximumPopulation([[1993,1999], [2000,2010]]))
print(s.maximumPopulation([[1950,1961], [1960,1971], [1970,1981]]))