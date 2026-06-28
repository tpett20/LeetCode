from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        counter = [0] * n
        extras = 0
        for num in arr:
            idx = num - 1
            if num <= n:
                counter[idx] += 1
            else:
                extras += 1
        max_el = 0
        for idx, freq in enumerate(counter):
            if not freq:
                continue
            num = idx + 1
            max_el = min(num, max_el + freq)
        return max_el + extras

s = Solution()
print(s.maximumElementAfterDecrementingAndRearranging([1,2,2,5,5,17]))