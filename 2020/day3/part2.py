import numpy as np
import json

with open("data.json") as f:
    data = np.array(json.load(f))

trees = 1

for j in [1, 3, 5, 7]:
    tmp = 0
    for i, d in enumerate(data):
        if d[i*j % len(d)] == '#':
            tmp += 1
    trees *= tmp

tmp = 0
for i, d in enumerate(data[::2]):
    if d[i % len(d)] == '#':
        tmp += 1
trees *= tmp

print(trees)
