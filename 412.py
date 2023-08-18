# 412. FizzBuzz
# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

def fizzBuzz(n):
    list = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            list.append('FizzBuzz')
        elif i % 3 == 0:
            list.append('Fizz')
        elif i % 5 == 0:
            list.append('Buzz')
        else: 
            list.append(f"{i}")
    return list

print(fizzBuzz(15))