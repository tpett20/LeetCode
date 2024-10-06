# 567. Permutation in String
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def get_perm_diff(dict1, dict2):
            difference = 0
            for key in dict2:
                if key not in dict1:
                    difference += dict2[key]
                elif dict2[key] > dict1[key]:
                    difference += (dict2[key] - dict1[key])
            return difference
        
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2:
            return False
        
        ltrs1 = {}
        for char in s1:
            if char in ltrs1:
                ltrs1[char] += 1
            else:
                ltrs1[char] = 1
        ltrs2 = {}
        for i in range(len1 - 1):
            char = s2[i]
            if char in ltrs2:
                ltrs2[char] += 1
            else:
                ltrs2[char] = 1
        
        diff = 0
        for i in range(len2 - len1 + 1):
            new_char = s2[i + len1 - 1]
            if new_char in ltrs2:
                ltrs2[new_char] += 1
            else:
                ltrs2[new_char] = 1
            if diff == 0:
                diff = get_perm_diff(ltrs1, ltrs2)
                if diff == 0:
                    return True
            diff -= 1
            old_char = s2[i]
            ltrs2[old_char] -= 1
            if ltrs2[old_char] == 0:
                del ltrs2[old_char]
        return False

s = Solution()
print(s.checkInclusion("ab", "eidbaooo"))
print(s.checkInclusion("ab", "eidboaoo"))
print(s.checkInclusion("rvwrk", "lznomzggwrvrkxecjaq"))