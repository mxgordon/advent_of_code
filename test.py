import json

with open('day3/data.json', 'r') as f:
    data = f.read().split(',')
with open('day3/data.json', 'w') as f:
    json.dump(data, f)