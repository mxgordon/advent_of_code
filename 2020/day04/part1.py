import json


with open("data.json", 'r') as f:
    data = json.load(f)

valid = 0
for passport in data:
    if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport):
        valid += 1

print(valid)
