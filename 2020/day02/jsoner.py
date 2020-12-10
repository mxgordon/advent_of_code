import json

with open("data.txt", 'r') as f:
    data = []
    for line in f:
        spt = line.split()
        parsed = [int(spt[0].split('-')[0]), int(spt[0].split('-')[1]), spt[1][0], spt[2]]
        data.append(parsed)

with open("data.json", 'w') as f:
    json.dump(data, f)
