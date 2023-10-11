# 2413. Smallest Even Multiple
# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

def smallestEvenMultiple(n):
    if n % 2 == 0:
        return n
    else:
        return n * 2
    
print(smallestEvenMultiple(5))
print(smallestEvenMultiple(6))