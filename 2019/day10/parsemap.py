import json


with open('map.txt', 'r') as f:
    lines = f.readlines()

final = []
tmp = []

for line in lines:
    for ele in line:
        if ele != '\n':
            print(ele)
            tmp.append(1 if ele == '#' else 0)
    final.append(tmp.copy())
    tmp.clear()

with open('data.json', 'w') as f:
    json.dump(final, f)