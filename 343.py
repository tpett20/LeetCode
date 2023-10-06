# 343. Integer Break
# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
# Return the maximum product you can get.

def integerBreak(n):
    if n <= 3:
        return n - 1
    k = 2
    max_product = 0
    while n // k > 1:
        integers = []
        quotient = n // k 
        remainder = n % k
        for _ in range(k):
            integers.append(quotient)
        for i in range(remainder):
            integers[i] += 1
        product = 1
        for int in integers:
            product *= int
        if product > max_product:
            max_product = product
        k += 1
    return max_product

print(integerBreak(2))
print(integerBreak(10))
print(integerBreak(11))