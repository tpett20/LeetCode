# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def isAnagram(s, t):
    if len(s) != len(t): return False
    map = {}
    for char in s:
        if map.get(char):
            map[char] += 1
        else:
            map[char] = 1
    for char in t:
        if map.get(char):
            map[char] -= 1
        else:
            return False
    return True

print(isAnagram('peach', 'cheap'))
print(isAnagram('to', 'two'))