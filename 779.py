# 779. K-th Symbol in Grammar
# 🚫 INCOMPLETE - Time Limit Exceeded
# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0
        row = '01'
        while len(row) < k:
            print(len(row))
            newRow = row
            for i in range(0, len(row), 2):
                pair = row[i:i+2]
                if pair == '01':
                    newRow += '10'
                else:
                    newRow += '01'
            row = newRow
        return int(row[k - 1])

s = Solution()
print(s.kthGrammar(2, 2))
print(s.kthGrammar(30, 434991989))