# 3014. Minimum Number of Pushes to Type Word I
# You are given a string word containing distinct lowercase English letters.
# Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .
# It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.
# Return the minimum number of pushes needed to type word after remapping the keys.

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = 0
        for i in range(len(word)):
            count += i // 8 + 1
        return count

s = Solution()
print(s.minimumPushes("abcdefghijklmnopqrstuvwxyz"))