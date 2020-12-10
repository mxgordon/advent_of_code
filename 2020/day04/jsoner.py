import json

with open("data.txt", 'r') as read:
    with open('data.json', 'w') as write:
        data = read.read().split('\n\n')
        data = [{s[:3]: s[4:] for s in d.split()} for d in data]
        json.dump(data, write)
