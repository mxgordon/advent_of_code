import json


with open("data.json", 'r') as f:
    data = json.load(f)

counter = 0
for line in data:
    first, second = line[3][line[0]-1] == line[2], line[3][line[1]-1] == line[2]

    if first != second:
        counter += 1

print(counter)
