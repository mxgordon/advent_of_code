import json

with open("data.json", 'w') as f1:
    with open("data.txt", 'r') as f2:
        json.dump([int(l) for l in f2], f1)