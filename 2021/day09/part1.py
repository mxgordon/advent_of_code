import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict, Counter

with open("data.txt", 'r') as f:
    data = f.readlines()
#     data = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678""".split("\n")

    data = np.array(list(map(lambda x: list(map(int, list(x))), map(str.strip, data))))

rshift = np.roll(data, 1, 1)
rshift[:, 0] = 10

lshift = np.roll(data, -1, 1)
lshift[:, -1] = 10

dshift = np.roll(data, 1, 0)
dshift[0] = 10

ushift = np.roll(data, -1, 0)
ushift[-1] = 10

shifts = np.stack((data-rshift, data-lshift, data-dshift, data-ushift), axis=0)
shifts[np.where(shifts >= 0)] = 99

print((data[np.where(shifts.sum(0) < 0)] + 1).sum())