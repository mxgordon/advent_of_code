with open("data.txt", 'r') as f:
    data = f.readlines()

data = [[{*range(int(e.split("-")[0]), int(e.split("-")[1]) + 1)} for e in d.split(",")] for d in data]
count = 0

for first, second in data:
    if len(first.intersection(second)) > 0:
        count += 1

print(count)
