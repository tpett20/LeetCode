# 1310. XOR Queries of a Subarray
# You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].
# For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).
# Return an array answer where answer[i] is the answer to the ith query.

from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre_xor = 0
        pre_xors = []
        for num in arr:
            pre_xor ^= num
            pre_xors.append(pre_xor)
        output = []
        for q in queries:
            lt, rt = q
            if lt == 0:
                output.append(pre_xors[rt])
            else:
                beg_xor = pre_xors[lt - 1]
                end_xor = pre_xors[rt]
                output.append(beg_xor ^ end_xor)
        return output

s = Solution()
print(s.xorQueries([1,3,4,8], [[0,1], [1,2], [0,3], [3,3]]))