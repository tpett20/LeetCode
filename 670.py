# 670. Maximum Swap
# You are given an integer num. You can swap two digits at most once to get the maximum valued number.
# Return the maximum valued number you can get.

class Solution:
    def maximumSwap(self, num: int) -> int:
        def join_num(arr):
            output = ""
            for num in arr:
                output += str(num)
            return int(output)
        
        nums = list(str(num))
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        for i in range(len(nums) - 1):
            rt_max = max(nums[i+1:])
            rt_max_idx = -1
            if rt_max > nums[i]:
                for j in range(i + 1, len(nums)):
                    if nums[j] == rt_max:
                        rt_max_idx = j
                nums[i], nums[rt_max_idx] = nums[rt_max_idx], nums[i]
                return join_num(nums)
        return num

s = Solution()
print(s.maximumSwap(9973))
print(s.maximumSwap(158365))