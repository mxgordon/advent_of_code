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

final = part_dos[zeros.index(min(zeros))]

print((final == 1).sum() * (final == 2).sum())