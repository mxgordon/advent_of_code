import json


with open("data.json", 'r') as f:
    data = json.load(f)

count = sum([len({*group}) for _, group in data])

print(count)
