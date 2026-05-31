# 2126. Destroying Asteroids
# You are given an integer mass, which represents the original mass of a planet. You are further given an integer array asteroids, where asteroids[i] is the mass of the ith asteroid.
# You can arrange for the planet to collide with the asteroids in any arbitrary order. If the mass of the planet is greater than or equal to the mass of the asteroid, the asteroid is destroyed and the planet gains the mass of the asteroid. Otherwise, the planet is destroyed.
# Return true if all asteroids can be destroyed. Otherwise, return false.

from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        s_asteroids = sorted(asteroids)
        for a in s_asteroids:
            if mass >= a:
                mass += a
            else:
                return False
        return True

s = Solution()
print(s.asteroidsDestroyed(1, [1,2,4,8,16,32,64]))
print(s.asteroidsDestroyed(1, [2,4,8,16,32,64]))