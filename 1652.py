# 1652. Defuse the Bomb
# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
    # If k > 0, replace the ith number with the sum of the next k numbers.
    # If k < 0, replace the ith number with the sum of the previous k numbers.
    # If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        output = []
        curr_sum = 0
        if k > 0:
            for i in range(k):
                curr_sum += code[i]
            for i in range(n):
                curr_sum += code[(i + k) % n]
                curr_sum -= code[i]
                output.append(curr_sum)
        else:
            for i in range(k - 1, -1):
                curr_sum += code[i]
            for i in range(n):
                curr_sum += code[i - 1]
                curr_sum -= code[i + k - 1]
                output.append(curr_sum)
        return output

s = Solution()
print(s.decrypt([1,9,6,9], 2))
print(s.decrypt([1,9,6,9], 0))
print(s.decrypt([1,9,6,9], -2))