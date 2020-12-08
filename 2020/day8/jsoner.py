import json


with open("data.txt", 'r') as read:
    with open("data.json", 'w') as write:
        json.dump([[line.strip().split()[0], int(line.strip().split()[1])] for line in read.readlines()], write)
