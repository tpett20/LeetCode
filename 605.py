# 605. Can Place Flowers
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

def canPlaceFlowers(flowerbed, n):
    if n == 0:
        return True
    if len(flowerbed) == 1:
        return True if flowerbed[0] == 0 else False
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        n -= 1
    if flowerbed[len(flowerbed) - 2] == 0 and flowerbed[len(flowerbed) - 1] == 0:
        flowerbed[len(flowerbed) - 1] = 1
        n -= 1
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            n -= 1
        if n < 0:
            return True
    return True if n == 0 else False

print(canPlaceFlowers([1,0,1,0,0], 1), 'Expected: True')
print(canPlaceFlowers([1,0,0,0,1], 2), 'Expected: False')
print(canPlaceFlowers([0,0,1,0,0], 1), 'Expected: True')