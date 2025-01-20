# 2661. First Completely Painted Row or Column
# You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].
# Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].
# Return the smallest index i at which either a row or a column will be completely painted in mat.

from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        pos_ref = {}
        for row in range(m):
            for col in range(n):
                val = mat[row][col]
                pos_ref[val] = [row, col]
        rows_fill = {}
        cols_fill = {}
        for i in range(len(arr)):
            val = arr[i]
            row, col = pos_ref[val]
            if row in rows_fill:
                rows_fill[row] += 1
            else:
                rows_fill[row] = 1
            if col in cols_fill:
                cols_fill[col] += 1
            else:
                cols_fill[col] = 1
            if rows_fill[row] == n or cols_fill[col] == m:
                return i

s = Solution()
print(s.firstCompleteIndex([1,3,4,2], [[1,4], [2,3]]))