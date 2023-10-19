# 1678. Goal Parser Interpretation
# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
# Given the string command, return the Goal Parser's interpretation of command.

class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        output = ''
        while i < len(command):
            if command[i] == 'G':
                output += 'G'
                i += 1
            elif command[i:i+2] == '()':
                output += 'o'
                i += 2
            else: 
                output += 'al'
                i += 4
        return output

s = Solution()
print(s.interpret("G()(al)"))
print(s.interpret("G()()()()(al)"))
print(s.interpret("(al)G(al)()()G"))