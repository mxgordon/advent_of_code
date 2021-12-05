import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict

with open("data.txt", 'r') as f:
    data = f.readlines()
    data = [[[*map(int, c.split(','))] for c in l.strip().split(" -> ")] for l in data]

floor = np.zeros((1000, 1000))

for start, end in data:
    if start[0] == end[0]:
        if start[1] < end[1]:
            floor[start[0], start[1]:end[1]+1] += 1
        else:
            floor[start[0], end[1]:start[1]+1] += 1
    elif start[1] == end[1]:
        if start[0] < end[0]:
            floor[start[0]:end[0]+1, start[1]] += 1
        else:
            floor[end[0]:start[0]+1, start[1]] += 1

print((floor > 1).sum())
