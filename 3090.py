# 3090. Maximum Length Substring With Two Occurrences
# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        m = {s[0]: 1}
        max_len = curr_len = 1
        i = 0
        for j in range(1, len(s)):
            curr_len += 1
            char = s[j]
            if char in m:
                m[char] += 1
                while m[char] > 2:
                    m[s[i]] -= 1
                    curr_len -= 1
                    i += 1
            else:
                m[char] = 1
            if curr_len > max_len:
                max_len = curr_len
        return max_len

s = Solution()
print(s.maximumLengthSubstring("bcbbbcba"))
print(s.maximumLengthSubstring("aaaa"))