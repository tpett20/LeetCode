# 869. Reordered Power of 2
# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.
# Return true if and only if we can do this so that the resulting number is a power of two.

class Solution:
    def are_anagrams(self, a: str, b: str) -> bool:
        a_map = {}
        b_map = {}
        for char in a:
            a_map[char] = a_map.get(char, 0) + 1
        for char in b:
            b_map[char] = b_map.get(char, 0) + 1
        if len(a_map) != len(b_map):
            return False
        for char in a_map:
            if a_map[char] != b_map.get(char, 0):
                return False
        return True

    def reorderedPowerOf2(self, n: int) -> bool:
        powers_of_2 = {}
        x = 1
        while x <= 10 ** 9:
            str_x = str(x)
            x_len = len(str_x)
            if x_len in powers_of_2:
                powers_of_2[x_len].append(str_x)
            else:
                powers_of_2[x_len] = [str_x]
            x *= 2
        str_n = str(n)
        n_len = len(str_n)
        power_options = powers_of_2.get(n_len, [])
        for power_of_2 in power_options:
            if self.are_anagrams(str_n, power_of_2):
                return True
        return False

s = Solution()
print(s.reorderedPowerOf2(4))
print(s.reorderedPowerOf2(80))
print(s.reorderedPowerOf2(856264354))