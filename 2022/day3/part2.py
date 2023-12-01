priorities = [*" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]

with open("data.txt", 'r') as f:
    data = f.read().split()

data = [set(d) for d in data]

points = []

for i in range(0, len(data), 3):
    print(i)
    first = data[i]
    second = data[i + 1]
    third = data[i + 2]
    points.append(priorities.index(list(first.intersection(second.intersection(third)))[0]))

print(sum(points))

