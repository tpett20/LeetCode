# 2767. Partition String Into Minimum Beautiful Substrings
# 🚫 INCOMPLETE - Biweekly Contest 108
# Given a binary string s, partition the string into one or more substrings such that each substring is beautiful.
# A string is beautiful if:
# It doesn't contain leading zeros.
# It's the binary representation of a number that is a power of 5.
# Return the minimum number of substrings in such partition. If it is impossible to partition the string s into beautiful substrings, return -1.
# A substring is a contiguous sequence of characters in a string.

def minimumBeautifulSubstrings(s):
    print(s)
    print(int(s,2))
    def powOfFive(num):
        print('called', num)
        if num % 5 != 0:
            print('not divisble')
            return False
        while num > 1:
            num = num / 5
            print('num', num)
            if num == 1: 
                print('TRUTH')
                return True
        return False
    start = 0
    end = len(s)
    output = 1
    print(powOfFive(int(s[start:end], 2)))
    while not powOfFive(int(s[start:end], 2)):
        if powOfFive(int(s[start-1:end], 2)):
            print('hit')
            start -= 1
            output += 1
        elif powOfFive(int(s[start:end-1], 2)):
            print('hit2')
            output += 1
            end -= 1
    return output

print(minimumBeautifulSubstrings('111'))