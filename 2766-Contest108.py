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


# relocateMarbles([1,6,7,8], [1,7,2], [2,9,5])
# relocateMarbles([1,1,3,3,15,12,20], [1,3], [2,2])
print(relocateMarbles([3,4], [4,3,1,2,2,3,2,4,1], [3,1,2,2,3,2,4,1,1]))