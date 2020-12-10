import json


with open("data.json", 'r') as f:
    data = json.load(f)

max_id = 0

for srow, scol in data:
    row = int(srow.replace("F", "0").replace("B", "1"), 2)
    col = int(scol.replace("L", "0").replace("R", "1"), 2)

    max_id = max(max_id, row*8 + col)

print(max_id)
