import random

res = []
for _ in range(50):
    res.append(random.randint(1, 50))
print(res)

# class Solution:
#     def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
#         def binary_search(target, arr):
#             # if target < arr[0]:
#             #     return 0
#             flr = 0
#             ceil = len(arr) - 1
#             while flr < ceil:
#                 mid = (flr + ceil) // 2
#                 if arr[mid] < target:
#                     flr = mid + 1
#                 elif arr[mid] > target:
#                     ceil = mid - 1
#                 else:
#                     return mid 
#             return flr
        
#         s_nums = sorted(nums)
#         # print(s_nums)
#         pairs = 0
#         for i in range(len(s_nums) - 1):
#             num = s_nums[i]
#             rem_arr = s_nums[i + 1:]
#             # print("NUM", num, rem_arr)
#             low = lower - num
#             high = upper - num
#             low_idx = binary_search(low, rem_arr)
#             if low <= rem_arr[low_idx] <= high:
#                 # print("LOW COUNTS")
#                 pairs += 1
#             high_idx = binary_search(high, rem_arr)
#             if low_idx != high_idx and low <= rem_arr[high_idx] <= high:
#                 # print("HIGH COUNTS")
#                 pairs += 1
#             # print("LOW", low, "idx", low_idx)
#             # print("HIGH", high, "idx", high_idx)
#             # print("BUMP", max(0, high_idx - low_idx - 1))
#             pairs += max(0, high_idx - low_idx - 1)
#             # print()
#         return pairs