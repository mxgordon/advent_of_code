import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict, Counter
from scipy import ndimage

with open("data.txt", 'r') as f:
    data = f.readlines()
    data = np.array([list(map(int, d.strip())) for d in data], dtype=int)

kernel = np.asarray([[True, True, True],
                     [True, False, True],
                     [True, True, True]])
one = np.ones(data.shape, dtype=int)
all_flashes = 0

for _ in range(100):
    data += one
    tens = data == 10
    flashed = np.empty(data.shape, dtype=bool)
    flashed.fill(False)
    while tens.any():
        tens = data >= 10
        for loc in zip(*np.where(tens)):
            solo = np.zeros(data.shape)
            solo[loc] = 1
            flashed[loc] = True

            data += ndimage.binary_dilation(solo, kernel)

        data[np.where(flashed)] = 0

    all_flashes += flashed.sum()

print(all_flashes)





