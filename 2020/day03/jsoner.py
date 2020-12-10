import json


with open("data.txt", 'r') as read:
    with open("data.json", 'w') as write:
        json.dump([[*line] for line in read.read().split()], write)
