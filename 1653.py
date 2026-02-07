# 1653. Minimum Deletions to Make String Balanced
# You are given a string s consisting only of characters 'a' and 'b'​​​​.
# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
# Return the minimum number of deletions needed to make s balanced.

class Solution:
    def minimumDeletions(self, s: str) -> int:
        lt_a = lt_b = 0
        rt_a = s.count("a")
        rt_b = s.count("b")
        min_dels = rt_a
        for char in s:
            if char == "a":
                lt_a += 1
                rt_a -= 1
            else:
                lt_b += 1
                rt_b -= 1
            min_dels = min(min_dels, lt_b + rt_a)
        return min_dels

s = Solution()
print(s.minimumDeletions("aababbab"))
print(s.minimumDeletions("aaabbb"))
print(s.minimumDeletions("bbbaaa"))