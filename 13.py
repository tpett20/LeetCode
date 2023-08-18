# 13. Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
    # I can be placed before V (5) and X (10) to make 4 and 9. 
    # X can be placed before L (50) and C (100) to make 40 and 90. 
    # C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

def roman_to_int(s):
    r_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
    total = r_nums[s[len(s)-1]]
    for i in range(len(s)-2, -1, -1):
        if r_nums[s[i]] >= r_nums[s[i+1]]:
            total += r_nums[s[i]]
        elif r_nums[s[i]] < r_nums[s[i+1]]:
            total -= r_nums[s[i]]
    return total
#41 ms

def roman_to_int(s):
    r_nums = [1, 5, 10, 50, 100, 500, 1000]
    idx_list = []
    for char in s:
        if char == 'I': idx_list.append(0)
        elif char == 'V': idx_list.append(1)
        elif char == 'X': idx_list.append(2)
        elif char == 'L': idx_list.append(3)
        elif char == 'C': idx_list.append(4)
        elif char == 'D': idx_list.append(5)
        else: idx_list.append(6)
    total = r_nums[idx_list[len(idx_list)-1]]
    for i in range(len(idx_list)-2, -1, -1):
        if r_nums[idx_list[i]] >= r_nums[idx_list[i+1]]:
            total += r_nums[idx_list[i]]
        elif r_nums[idx_list[i]] < r_nums[idx_list[i+1]]:
            total -= r_nums[idx_list[i]]
    return total
#53 ms 


# TEST CASES

r='LVIII'
print(f'{r} > {roman_to_int(r)} = 58')

r='LV'
print(f'{r} > {roman_to_int(r)} = 55')

r='XXXIX'
print(f'{r} > {roman_to_int(r)} = 39')

r='CCXLVI'
print(f'{r} > {roman_to_int(r)} = 246')

r='MLXVI'
print(f'{r} > {roman_to_int(r)} = 1066')

r='MLXIV'
print(f'{r} > {roman_to_int(r)} = 1064')

r='I'
print(f'{r} > {roman_to_int(r)} = 1')

r='II'
print(f'{r} > {roman_to_int(r)} = 2')

r='V'
print(f'{r} > {roman_to_int(r)} = 5')

r='X'
print(f'{r} > {roman_to_int(r)} = 10')

r='L'
print(f'{r} > {roman_to_int(r)} = 50')

r='C'
print(f'{r} > {roman_to_int(r)} = 100')

r='D'
print(f'{r} > {roman_to_int(r)} = 500')

r='M'
print(f'{r} > {roman_to_int(r)} = 1000')