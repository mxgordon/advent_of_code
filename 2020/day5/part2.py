import math
import json


with open("data.json", 'r') as f:
    data = json.load(f)

ids = []

for srow, scol in data:
    row = int(srow.replace("F", "0").replace("B", "1"), 2)
    col = int(scol.replace("L", "0").replace("R", "1"), 2)

    if row not in [0, 127]:
        ids.append(row*8 + col)

ids.sort()

for i, id_ in enumerate(ids[:-1]):
    if id_ + 2 == ids[i+1]:
        print(id_+1)
