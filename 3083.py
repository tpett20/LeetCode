# 3083. Existence of a Substring in a String and Its Reverse
# Given a string s, find any substring of length 2 which is also present in the reverse of s.
# Return true if such a substring exists, and false otherwise.

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        sub_strs_seen = set()
        for i in range(len(s) - 1):
            sub_str = s[i] + s[i + 1]
            sub_strs_seen.add(sub_str)
            rev_sub_str = s[i + 1] + s[i]
            if rev_sub_str in sub_strs_seen:
                return True
        return False

s = Solution()
print(s.isSubstringPresent("leetcode"))