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

colors = np.zeros(data.shape)

current = 1
all_colors = set()

for i, row in enumerate(data):
    for j, ele in enumerate(row):
        if ele == 9:
            current += 1
            continue
        else:
            colors[i, j] = current
            all_colors.add(current)
    current += 1

    if i != 0:
        for j, ele in enumerate(row):
            if colors[i-1, j] != 0 and colors[i, j] != 0:
                colors[np.where(colors == colors[i, j])] = colors[i-1, j]

sizes = sorted([int((colors == c).sum()) for c in all_colors], reverse=True)
print(reduce(int.__mul__, sizes[:3]))
#640305
