import json


with open("data.txt", 'r') as read:
    with open("data.json", 'w') as write:
        json.dump([[len(group.split()), ''.join(group.split())] for group in read.read().split(
            "\n\n")], write)
