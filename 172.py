# 172. Factorial Trailing Zeroes
# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

def trailingZeroes(n):
    factorial = 1
    while n >= 1:
        print(factorial, n)
        factorial *= n
        n -= 1
    zeroes = 0
    while factorial % 10 == 0:
        zeroes += 1
        factorial = factorial // 10
    return zeroes

print(trailingZeroes(20))