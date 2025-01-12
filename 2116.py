# 2116. Check if a Parentheses String Can Be Valid
# A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:
    # It is ().
    # It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
    # It can be written as (A), where A is a valid parentheses string.
# You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,
    # If locked[i] is '1', you cannot change s[i].
    # But if locked[i] is '0', you can change s[i] to either '(' or ')'.
# Return true if you can make s a valid parentheses string. Otherwise, return false.

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        locked_stack = []
        free_stack = []
        for i in range(n):
            is_locked = locked[i] == "1"
            if not is_locked:
                free_stack.append(i)
                continue
            if s[i] == "(":
                locked_stack.append(i)
            else:
                if locked_stack:
                    locked_stack.pop()
                elif free_stack:
                    free_stack.pop()
                else:
                    return False
        while locked_stack:
            locked_idx = locked_stack.pop()
            if not free_stack:
                return False
            free_idx = free_stack.pop()
            if free_idx < locked_idx:
                return False
        return True

s = Solution()
print(s.canBeValid(
    "))()))",
    "010100"
))
print(s.canBeValid(
    "((()(()()))()((()()))))()((()(()",
    "10111100100101001110100010001001"
))
print(s.canBeValid(
    "((((((",
    "111000"
))
print(s.canBeValid(
    "))))))",
    "000111"
))