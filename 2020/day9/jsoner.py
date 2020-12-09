import json


with open("data.txt", 'r') as read:
    with open("data.json", 'w') as write:
        json.dump([int(line) for line in read.readlines()], write)
