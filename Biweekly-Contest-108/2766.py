# 2766. Relocate Marbles
# 🏆 Biweekly Contest 108
# You are given a 0-indexed integer array nums representing the initial positions of some marbles. You are also given two 0-indexed integer arrays moveFrom and moveTo of equal length.
# Throughout moveFrom.length steps, you will change the positions of the marbles. On the ith step, you will move all marbles at position moveFrom[i] to position moveTo[i].
# After completing all the steps, return the sorted list of occupied positions.
# Notes:
# We call a position occupied if there is at least one marble in that position.
# There may be multiple marbles in a single position.

def relocateMarbles(nums, moveFrom, moveTo):
    map = {}
    for i in range(len(nums)):
        print(map)
        if map.get(nums[i]):
            map[nums[i]] += 1
        else: 
            map[nums[i]] = 1
    print('map filled', map)
    for i in range(len(moveFrom)):
        fro = moveFrom[i]
        to = moveTo[i]
        print(map, fro, '->', to)
        if fro != to: 
            if map.get(to):
                map[to] += map[fro]
            else:
                map[to] = map[fro]
            map[fro] = 0
    print(map)
    output = []
    for key in map:
        if map[key]:
            output.append(key)
    output.sort()
    return output


print(relocateMarbles([1,6,7,8], [1,7,2], [2,9,5]))
print(relocateMarbles([1,1,3,3,15,12,20], [1,3], [2,2]))
print(relocateMarbles([3,4], [4,3,1,2,2,3,2,4,1], [3,1,2,2,3,2,4,1,1]))