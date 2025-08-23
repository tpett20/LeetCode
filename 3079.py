# 3079. Find the Sum of Encrypted Integers
# You are given an integer array nums containing positive integers. We define a function encrypt such that encrypt(x) replaces every digit in x with the largest digit in x. For example, encrypt(523) = 555 and encrypt(213) = 333.
# Return the sum of encrypted elements.

from typing import List

class Solution:
    def encrypt(self, num: int) -> int:
        encrypted_num = 0
        num_digits = 0
        max_digit = 0
        while num > 0:
            num_digits += 1
            max_digit = max(max_digit, num % 10)
            num //= 10
        for i in range(num_digits):
            encrypted_num += max_digit * 10 ** i
        return encrypted_num

    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        encrypted_sum = 0
        for num in nums:
            encrypted_sum += self.encrypt(num)
        return encrypted_sum

s = Solution()
print(s.sumOfEncryptedInt([123, 345, 567, 789, 910]))