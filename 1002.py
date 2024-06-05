# 1002. Find Common Characters
# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        main_map = {}
        for char in words[0]:
            if char in main_map:
                main_map[char] += 1
            else:
                main_map[char] = 1
        for i in range(1, len(words)):
            word = words[i]
            curr_map = {}
            for char in word:
                if char in curr_map:
                    curr_map[char] += 1
                else:
                    curr_map[char] = 1
            main_keys = list(main_map.keys())
            for char in main_keys:
                if char in curr_map:
                    main_map[char] = min(main_map[char], curr_map[char])
                else:
                    del main_map[char]
        output = []
        for char in main_map:
            freq = main_map[char]
            for _ in range(freq):
                output.append(char)
        return output

s = Solution()
print(s.commonChars(["bella", "label", "roller"]))
print(s.commonChars(["cool", "lock", "cook"]))