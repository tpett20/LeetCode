# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

def reverseWords(s):
    i = len(s) - 1
    floor = 0
    subStr = ''
    string = ''
    while s[i] == ' ':
        i -= 1
    while s[floor] == ' ':
        floor += 1
    while i >= floor:
        if s[i] != ' ':
            subStr = s[i] + subStr
        elif s[i] == ' ' and s[i + 1] != ' ':
            string += subStr + ' '
            subStr = ''
        i -= 1
    string += subStr
    return string

print(reverseWords("a good   example"))