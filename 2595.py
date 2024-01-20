# 2595. Number of Even and Odd Bits
# You are given a positive integer n.
# Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.
# Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.
# Return an integer array answer where answer = [even, odd].

class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        output = [0, 0]
        even = True
        while n > 0:
            r = n % 2
            if r:
                if even:
                    output[0] += 1
                else:
                    output[1] += 1
            n = n // 2
            even = not even
        return output

s = Solution()
print(s.evenOddBit(17))
print(s.evenOddBit(2))