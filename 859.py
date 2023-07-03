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
    diffS = ''
    diffGoal = ''
    swap = False
    for i in range(len(s)):
        if s[i] != goal[i]:
            if swap: return False
            if diffS and diffGoal:
                if s[i] == diffGoal and goal[i] == diffS:
                    swap = True
                else: return False
            else:
                diffS = s[i]
                diffGoal = goal[i]
    return swap

print(buddyStrings("ab", "ba"))
print(buddyStrings("apple", "apple"))
print(buddyStrings("rapple", "appler"))
print(buddyStrings("pear", "paer"))