priorities = [*" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]

with open("data.txt", 'r') as f:
    data = f.read().split()

data = [(set(d[:len(d) // 2]), set(d[len(d) // 2:])) for d in data]
shared = [list(a.intersection(b))[0] for a, b in data]
shared_points = [priorities.index(e) for e in shared]

print(sum(shared_points))

