import json


with open("data.json", 'r') as f:
    data = json.load(f)

count = 0
for num, group in data:
    count += len({*group})

print(count)
