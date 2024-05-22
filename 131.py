# 131. Palindrome Partitioning
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pals = {}
        for char in s:
            pals[char] = True
        
        def check_pal(string):
            if string in pals:
                return True if pals[string] else False
            l, r = 0, len(string) - 1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        output = []
        def traverse(string, remain, arr):
            if check_pal(string):
                arr.append(string)
            else:
                return
            if not len(remain):
                output.append(arr)
            else:
                for i in range(len(remain)):
                    traverse(remain[:i + 1], remain[i + 1:], arr.copy())
        
        for i in range(len(s)):
            traverse(s[:i + 1], s[i + 1:], [])
        return output


s = Solution()
print(s.partition("aab"))
print(s.partition("a"))