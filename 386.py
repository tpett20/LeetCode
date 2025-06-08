# 386. Lexicographical Numbers
# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
# You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

from typing import List

class Solution:
    def __init__(self):
        self.res = []
        self.max_num = None
        self.max_len = None
    
    def traverse(self, curr: str) -> None:
        if curr == "0":
            return
        if curr:
            self.res.append(int(curr))
        for i in range(10):
            nxt = curr + str(i)
            if len(nxt) > self.max_len or int(nxt) > self.max_num:
                break
            self.traverse(nxt)
    
    def lexicalOrder(self, n: int) -> List[int]:
        self.max_num = n
        self.max_len = len(str(n))
        self.traverse("")
        return self.res

s = Solution()
print(s.lexicalOrder(1969))