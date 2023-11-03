# 1441. Build an Array With Stack Operations
# You are given an integer array target and an integer n.
# You have an empty stack with the two following operations:
# - "Push": pushes an integer to the top of the stack.
# - "Pop": removes the integer on the top of the stack.
# You also have a stream of the integers in the range [1, n].
# Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target. You should follow the following rules:
# - If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.
# - If the stack is not empty, pop the integer at the top of the stack.
# - If, at any moment, the elements in the stack (from the bottom to the top) are equal to target, do not read new integers from the stream and do not do more operations on the stack.
# Return the stack operations needed to build target following the mentioned rules. If there are multiple valid answers, return any of them.

class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        stack_ops = []
        i = 0
        num = 1
        while i < len(target):
            stack_ops.append('Push')
            if num == target[i]:
                i += 1
            else:
                stack_ops.append('Pop')
            num += 1
        return stack_ops

s = Solution()
print(s.buildArray([1,3], 3))
print(s.buildArray([1,2,3], 3))
print(s.buildArray([1,2], 4))