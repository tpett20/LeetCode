# 859. Buddy Strings
# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

def buddyStrings(s, goal):
    if len(s) != len(goal): return False
    if s == goal:
        map = {}
        for i in range(len(s)):
            if map.get(s[i]): return True
            else: map[s[i]] = True
        return False
    sMap = {}
    goalMap = {}
    swap = False
    diffs = 0
    for i in range(len(s)):
        if s[i] != goal[i]:
            diffs += 1
            if diffs > 2: return False
            if swap: return False
            if sMap.get(goal[i]) and goalMap.get(s[i]):
                swap = True
            elif not sMap.get(s[i]) and not goalMap.get(goal[i]):
                sMap[s[i]] = True
                goalMap[goal[i]] = True
    return swap

print(buddyStrings("ab", "ba"))
print(buddyStrings("apple", "apple"))
print(buddyStrings("rapple", "appler"))
print(buddyStrings("pear", "paer"))