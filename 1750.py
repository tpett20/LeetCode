# 1750. Minimum Length of String After Deleting Similar Ends
# Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:
    # Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
    # Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
    # The prefix and the suffix should not intersect at any index.
    # The characters from the prefix and suffix must be the same.
    # Delete both the prefix and the suffix.
# Return the minimum length of s after performing the above operation any number of times (possibly zero times).

class Solution:
    def minimumLength(self, s: str) -> int:
        pre = 0
        suf = len(s) - 1
        rule = s[pre]
        while pre < suf and rule == s[pre] == s[suf]:
            while pre < len(s) and s[pre] == rule:
                pre += 1
            while suf >= 0 and s[suf] == rule:
                suf -= 1
            if pre < len(s):
                rule = s[pre]
            else:
                break
        return 0 if pre > suf else suf - pre + 1

s = Solution()
print(s.minimumLength("ca"))
print(s.minimumLength("cabaabac"))
print(s.minimumLength("aabccabba"))