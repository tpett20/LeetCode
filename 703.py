# 703. Kth Largest Element in a Stream
# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Implement KthLargest class:
# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = sorted(nums)
        self.k = k
   
    def find_insert_idx(self, val):
        flr = 0
        ceil = len(self.stream) - 1
        while flr <= ceil:
            mid = (flr + ceil) // 2
            if val < self.stream[mid]:
                ceil = mid - 1
            elif val > self.stream[mid]:
                flr = mid + 1
            else:
                return mid
        return flr

    def add(self, val: int) -> int:
        idx = self.find_insert_idx(val)
        self.stream.insert(idx, val)
        return self.stream[len(self.stream) - self.k]


obj = KthLargest(3, [4,5,8,2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))