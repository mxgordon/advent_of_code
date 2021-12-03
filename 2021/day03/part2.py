import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict

with open("data.txt", 'r') as f:
    data = f.readlines()
    data = [[int(a) for a in d.strip()] for d in data]
    # data = np.array(data)

tmpd = data.copy()
ones = []
zeros = []
for i in range(len(tmpd[0])):
    for line in tmpd:
        if line[i] == 0:
            zeros.append(line)
        else:
            ones.append(line)
    if len(ones) >= len(zeros):
        tmpd = ones
    else:
        tmpd = zeros

    ones, zeros = [], []
    print(len(tmpd))

    if len(tmpd) == 1:
        break
oxy = int("".join(map(str, tmpd[0])), 2)

tmpd = data.copy()
ones = []
zeros = []
for i in range(len(tmpd[0])):
    for line in tmpd:
        if line[i] == 0:
            zeros.append(line)
        else:
            ones.append(line)
    if len(ones) < len(zeros):
        tmpd = ones
    else:
        tmpd = zeros

    ones, zeros = [], []
    print(len(tmpd))
    if len(tmpd) == 1:
        break

co2 = int("".join(map(str, tmpd[0])), 2)
print(co2 * oxy, co2, oxy)
