import json


with open("data.txt", 'r') as read:
    with open("data.json", 'w') as write:
        json.dump([[line[:-3], line[-3:]] for line in read.read().split()], write)
