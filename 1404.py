# 1404. Number of Steps to Reduce a Number in Binary Representation to One
# Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
    # If the current number is even, you have to divide it by 2.
    # If the current number is odd, you have to add 1 to it.
# It is guaranteed that you can always reach one for all test cases.

class Solution:
    def numSteps(self, s: str) -> int:
        def add_one(arr):
            i = len(arr) - 1
            while i >= 0 and arr[i] == "1":
                arr[i] = "0"
                i -= 1
            if i < 0:
                arr[0] = "1"
                arr.append("0")
            else:
                arr[i] = "1"
        
        num = list(s)
        steps = 0
        while len(num) > 1:
            if num[-1] == "0":
                num.pop()
            else:
                add_one(num)
            steps += 1
        return steps

s = Solution()
print(s.numSteps("1011"))
print(s.numSteps("10"))
print(s.numSteps("1"))