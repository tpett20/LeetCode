# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):
    if not len(s): return 0
    max_length = 1
    for i in range(len(s)-1):
        map = {s[i]: 1}
        next = i + 1
        count = 1
        while next < len(s) and not map.get(s[next]):
            count += 1
            if count > max_length:
                max_length = count
            map[s[next]] = 1
            next += 1
    return max_length

print(lengthOfLongestSubstring('abcabcbb'))