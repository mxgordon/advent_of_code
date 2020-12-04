import json


with open("data.json", 'r') as f:
    data = json.load(f)

valid = 0
for d in data:
    if len(d) == 8 or (len(d) == 7 and 'cid' not in d):
        valid += 1

print(valid)
