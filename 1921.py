# 1921. Eliminate Maximum Number of Monsters
# You are playing a video game where you are defending your city from a group of n monsters. You are given a 0-indexed integer array dist of size n, where dist[i] is the initial distance in kilometers of the ith monster from the city.
# The monsters walk toward the city at a constant speed. The speed of each monster is given to you in an integer array speed of size n, where speed[i] is the speed of the ith monster in kilometers per minute.
# You have a weapon that, once fully charged, can eliminate a single monster. However, the weapon takes one minute to charge. The weapon is fully charged at the very start.
# You lose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon is fully charged, it counts as a loss, and the game ends before you can use your weapon.
# Return the maximum number of monsters that you can eliminate before you lose, or n if you can eliminate all the monsters before they reach the city.

import math

class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        times_to_city = []
        for i in range(len(dist)):
            time = math.ceil(dist[i] / speed[i])
            times_to_city.append(time)
        times_to_city.sort()
        minute = 0
        monsters = 0
        for time in times_to_city:
            if minute < time:
                monsters += 1
            else:
                break
            minute += 1
        return monsters

s = Solution()
print(s.eliminateMaximum([1,3,4], [1,1,1]))
print(s.eliminateMaximum([1,1,2,3], [1,1,1,1]))
print(s.eliminateMaximum([3,2,4], [5,3,2]))
print(s.eliminateMaximum([3,5,7,4,5], [2,3,6,3,2]))