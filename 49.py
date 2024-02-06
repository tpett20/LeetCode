# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def get_tuple_key(string):
            arr = [0] * 26
            for char in string:
                idx = ord(char) - 97
                arr[idx] += 1
            return tuple(arr)
        
        groups = {}
        for word in strs:
            key = get_tuple_key(word)
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return groups.values()

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))