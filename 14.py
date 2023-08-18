# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):
    for i in range(len(strs[0])-1, -2, -1):
        prefix = strs[0][0:i+1]
        print(f"prefix: {prefix}")
        count = 0
        for j in range(0, len(strs)):
            if strs[j][0:i+1] == prefix:
                prefix = strs[j][0:i+1]
                count += 1
            if count == len(strs):
                return prefix

print(longestCommonPrefix(["a"]))
print(longestCommonPrefix(["dog","acecar","dcar"]))