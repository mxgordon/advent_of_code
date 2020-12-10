import json

with open("data.json", 'r') as f:
    data = json.load(f)

for i, n in enumerate(data):
    for n2 in data[i:]:
        if n + n2 == 2020:
            print(n, n2, n*n2)