import json


with open("data.json", 'r') as f:
    data = json.load(f)

count = 0
for num, group in data:
    for letter in [*'qwertyuiopasdfghjklzxcvbnm']:
        if group.count(letter) == num:
            count += 1

print(count)
