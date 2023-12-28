# 443. String Compression
# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# - If the group's length is 1, append the character to s.
# - Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.

class Solution:
    def compress(self, chars: list[str]) -> int:
        chars.append(None)
        i = 0
        consec_len = 1
        for j in range(1, len(chars)):
            if chars[j] != chars[j - 1]:
                chars[i] = chars[j - 1]
                i += 1
                if consec_len > 1:
                    consec_len = str(consec_len)
                    for digit in consec_len:
                        chars[i] = digit
                        i += 1
                    consec_len = 1
            else:
                consec_len += 1
        for _ in range(i, len(chars)):
            chars.pop()
        return i

s = Solution()
test_case1 = ["a","a","b","b","c","c","c"]
print(s.compress(test_case1))
print(test_case1)

test_case2 = ["a"]
print(s.compress(test_case2))
print(test_case2)

test_case3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(s.compress(test_case3))
print(test_case3)