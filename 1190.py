# 1190. Reverse Substrings Between Each Pair of Parentheses
# You are given a string s that consists of lower case English letters and brackets.
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
# Your result should not contain any brackets.

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            char = s[i]
            if char != ")":
                stack.append(char)
                continue
            rev = []
            while stack[-1] != "(":
                rev.append(stack.pop())
            stack.pop()
            stack.extend(rev)
        return "".join(stack)