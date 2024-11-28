import random

arr = [1, 2, 3, 4, 5, 0]

random.shuffle(arr)
new_arr = []
i = 0
for r in range(2):
    new_row = []
    for c in range(3):
        new_row.append(arr[i])
        i += 1
    new_arr.append(new_row)
print(new_arr)