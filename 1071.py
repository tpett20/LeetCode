# 1071. Greatest Common Divisor of Strings
# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

def gcdOfStrings(str1, str2):
    factor = len(str1) if len(str1) < len(str2) else len(str2)
    while factor >= 1:
        if len(str1) % factor == 0 and len(str2) % factor == 0:
            divisor = str1[0 : factor]
            longerLen = len(str1) if len(str1) > len(str2) else len(str2)
            i = 0
            j = 0
            while i < len(str1) or i < len(str2):
                if i < len(str1) and i < len(str2):
                    if str1[i] != divisor[j] or str2[i] != divisor[j]:
                        return ''
                elif i < len(str1):
                    if str1[i] != divisor[j]:
                        return ''
                else: 
                    if str2[i] != divisor[j]:
                        return ''
                i += 1
                j += 1
                if j == len(divisor): j = 0
            if i == longerLen: return divisor
        factor -= 1

print(gcdOfStrings('A', 'AA'))
print(gcdOfStrings('ABABAB', 'ABAB'))