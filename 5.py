class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        if len(s) == 2: 
            if s[0] == s[1]: return s
            else: return s[0]

        def get_pal(substr, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                substr = s[left] + substr + s[right]
                left -= 1
                right += 1
            return substr

        longest_pal = s[:2] if s[0] == s[1] else s[0]
        i = 1
        remaining_chars = len(s) - 2
        while remaining_chars >= len(longest_pal) / 2:
            pal = get_pal(s[i], i - 1, i + 1)
            if len(pal) > len(longest_pal):
                longest_pal = pal
            if s[i] == s[i + 1]:
                pal = get_pal(s[i:i+2], i - 1, i + 2)
                if len(pal) > len(longest_pal):
                    longest_pal = pal
            i += 1
            remaining_chars = len(s) - 1 - i
        return longest_pal

s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))