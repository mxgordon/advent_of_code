import numpy as np
import collections
import json


with open('data.json', 'r') as f:
    nums = json.load(f)


part_uno = []
part_dos = []


for i in range(len(nums) // 25):
    part_uno.append(nums[25 * i: 25 * (i + 1)])

for i in range(len(part_uno) // 6):
    part_dos.append(part_uno[6 * i: 6 * (i+1)])

part_dos = np.array(part_dos)

current = None
zeros = []

for group in part_dos:
    zeros.append((group == 0).sum())

final = np.ndarray((6, 25)).astype(int)
final.fill(-1)

for layer in part_dos:
    for y, x_line in enumerate(layer):
        for x, val in enumerate(x_line):
            if val != 2 and final[y][x] == -1:
                final[y][x] = val



for i in final:
    print(*i, sep='', end='')
print('\n')
print(final)