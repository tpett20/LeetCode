# 844. Backspace String Compare
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        typedS = ''
        backspaces = 0
        while i >= 0:
            if s[i] == '#':
                backspaces += 1
            elif backspaces:
                backspaces -= 1
            else:
                typedS += s[i]
            i -= 1
        i = len(t) - 1
        typedT = ''
        backspaces = 0
        while i >= 0:
            if t[i] == '#':
                backspaces += 1
            elif backspaces:
                backspaces -= 1
            else:
                typedT += t[i]
            i -= 1
        return typedS == typedT

s = Solution()
print(s.backspaceCompare('ab#c', 'ad#c'))
print(s.backspaceCompare('ab##', 'c#d#'))
print(s.backspaceCompare('a#c', 'b'))