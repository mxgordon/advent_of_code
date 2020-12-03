import numpy as np
import json

with open("data.json") as f:
    data = np.array(json.load(f))

trees = 0

for i, d in enumerate(data):
    if d[i * 3 % len(d)] == '#':
        trees += 1

print(trees)
