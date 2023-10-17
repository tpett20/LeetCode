# 118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it:

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        output = [[1]]

        def addNextRow(target, count = 1, row = [1]):
            if target == count:
                return
            newRow = [1]
            for i in range(1, len(row)):
                newRow.append(row[i] + row[i - 1])
            newRow.append(1)
            output.append(newRow)
            addNextRow(target, count + 1, newRow)

        addNextRow(numRows)
        return output

s = Solution()
print(s.generate(5))
print(s.generate(1))