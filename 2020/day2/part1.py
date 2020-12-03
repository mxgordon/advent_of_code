import json


with open("data.json", 'r') as f:
    data = json.load(f)

counter = 0
for line in data:
    if line[0] <= line[3].count(line[2]) <= line[1]:
        counter += 1

print(counter)
