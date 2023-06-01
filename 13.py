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