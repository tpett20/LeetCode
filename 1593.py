# 1593. Split a String Into the Max Number of Unique Substrings
# Given a string s, return the maximum number of unique substrings that the given string can be split into.
# You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.
# A substring is a contiguous sequence of characters within a string.

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def traverse(r=""):
            if r == "":
                return len(seen)
            max_count = 0
            for i in range(1, len(r)+1):
                sub_str = r[:i]
                leftover = r[i:]
                if sub_str not in seen:
                    seen.add(sub_str)
                    count = traverse(leftover)
                    max_count = max(max_count, count)
                    seen.remove(sub_str)
            return max_count

        seen = set()
        return traverse(s)

s = Solution()
print(s.maxUniqueSplit("ababccc"))