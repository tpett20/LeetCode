# 1160. Find Words That Can Be Formed by Characters
# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_map = {}
        for char in chars:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1
        
        def check_word(word):
            map = char_map.copy()
            for char in word:
                if char not in map or map[char] == 0:
                    return False
                else:
                    map[char] -= 1
            return True
        
        sum = 0
        for word in words:
            if check_word(word):
                sum += len(word)
        return sum

s = Solution()
print(s.countCharacters(["cat","bt","hat","tree"], "atach"))
print(s.countCharacters(["hello","world","leetcode"], "welldonehoneyr"))