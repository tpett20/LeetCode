# 205. Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

def isIsomorphic(s, t):
    map = {}
    for i in range(len(s)):
        val = map.get(s[i], 'empty')
        if val == 'empty':
            map[s[i]] = t[i]
        elif val != t[i]:
            return False
    map = {}
    for i in range(len(s)):
        val = map.get(t[i], 'empty')
        if val == 'empty':
            map[t[i]] = s[i]
        elif val != s[i]:
            return False
    return True

print(isIsomorphic('badc', 'baba'))            