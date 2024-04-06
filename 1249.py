# 1249. Minimum Remove to Make Valid Parentheses
# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
    # It is the empty string, contains only lowercase characters, or
    # It can be written as AB (A concatenated with B), where A and B are valid strings, or
    # It can be written as (A), where A is a valid string.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = 0
        output = ""
        for char in s:
            if char == "(":
                stack += 1
            elif char == ")":
                if stack:
                    stack -= 1
                else:
                    continue
            output += char
        if not stack:
            return output
        i = len(output) - 1
        f_output = ""
        while stack:
            if output[i] == "(":
                stack -= 1
            else:
                f_output = output[i] + f_output
            i -= 1
        return output[:i + 1] + f_output

s = Solution()
print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
print(s.minRemoveToMakeValid("a)b(c)d"))
print(s.minRemoveToMakeValid("))(("))
print(s.minRemoveToMakeValid("(a)(b"))