# 1743. Restore the Array From Adjacent Pairs
# There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.
# You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.
# It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.
# Return the original array nums. If there are multiple solutions, return any of them.

class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        map = {}
        for pair in adjacentPairs:
            if pair[0] in map:
                map[pair[0]].append(pair[1])
            else:
                map[pair[0]] = [pair[1]]
            if pair[1] in map:
                map[pair[1]].append(pair[0])
            else:
                map[pair[1]] = [pair[0]]
        output = []
        for key in map:
            if len(map[key]) == 1:
                output.append(int(key))
                output.append(map[key][0])
                break
        second_last_num = output[0]
        last_num = output[1]
        while len(output) < len(adjacentPairs) + 1:
            if map[last_num][0] != second_last_num:
                output.append(map[last_num][0])
                second_last_num = last_num
                last_num = map[last_num][0]
            else:
                output.append(map[last_num][1])
                second_last_num = last_num
                last_num = map[last_num][1]
        return output

s = Solution()
print(s.restoreArray([[2,1], [3,4], [3,2]]))
print(s.restoreArray([[4,-2], [1,4], [-3,1]]))
print(s.restoreArray([[100000,-100000]]))