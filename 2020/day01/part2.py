import json

with open("data.json", 'r') as f:
    data = json.load(f)

for i, n1 in enumerate(data):
    for j, n2 in enumerate(data[i:]):
        for n3 in data[i+j:]:
            if n1 + n2 + n3 == 2020:
                print(n1, n2, n3, n1*n2*n3)