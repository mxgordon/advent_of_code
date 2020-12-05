import math
import json


with open("data.json", 'r') as f:
    data = json.load(f)

ids = []

for srow, scol in data:
    row_min = 0
    row_max = 127
    for line in srow:
        move_to = row_min + (row_max-row_min)/2
        if line == "F":
            row_max = math.floor(move_to)
        else:
            row_min = math.ceil(move_to)
    row = row_min

    col_min = 0
    col_max = 7

    for line in scol:
        move_to = col_min + (col_max-col_min)/2
        if line == "L":
            col_max = math.floor(move_to)
        else:
            col_min = math.ceil(move_to)

    col = col_min

    if row not in [0, 127]:
        ids.append(row*8 + col)

ids.sort()

for i, id_ in enumerate(ids[:-1]):
    if id_ + 2 == ids[i+1]:
        print(id_+1)
