# 1415. The k-th Lexicographical String of All Happy Strings of Length n
# A happy string is a string that:
    # consists only of letters of the set ['a', 'b', 'c'].
    # s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
# Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
# Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

class Solution:
    def __init__(self):
        self.happy_strings = []

    def find_all_strings(self, curr: str, target: int) -> None:
        if len(curr) == target:
            self.happy_strings.append(curr)
            return
        letters = "abc"
        for ltr in letters:
            if curr and ltr == curr[-1]:
                continue
            self.find_all_strings(curr + ltr, target)

    def getHappyString(self, n: int, k: int) -> str:
        self.find_all_strings("", n)
        if len(self.happy_strings) < k:
            return ""
        return self.happy_strings[k - 1]

s = Solution()
print(s.getHappyString(1, 3))
print(s.getHappyString(10, 100))