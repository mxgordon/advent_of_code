from collections import defaultdict

with open("data.txt") as f:
    lines = f.read().strip("\n").split("\n")
    data = [list(line) for line in lines]


moves = [(i, j, k) for i in range(-1, 2) for j in range(-1, 2) for k in range(-1, 2) if (i, j, k) != (0, 0, 0)]

state = defaultdict(lambda: False)

n = m = 8

for i in range(n):
    for j in range(m):
        state[i, j, 0] = ("#" == data[i][j])


def step(d):
    dim = d.copy()

    minx = min(k[0] for k in d)
    maxx = max(k[0] for k in d)

    miny = min(k[1] for k in d)
    maxy = max(k[1] for k in d)

    minz = min(k[2] for k in d)
    maxz = max(k[2] for k in d)

    for x in range(minx - 1, maxx + 2):
        for y in range(miny - 1, maxy + 2):
            for z in range(minz - 1, maxz + 2):
                ac = 0
                for dx, dy, dz in moves:
                    if d[x + dx, y + dy, z + dz]:
                        ac += 1
                if d[x, y, z]:
                    if ac in (2, 3):
                        dim[x, y, z] = True
                    else:
                        dim[x, y, z] = False
                else:
                    if ac == 3:
                        dim[x, y, z] = True
                    else:
                        dim[x, y, z] = False
    return dim


for _ in range(6):
    state = step(state)

print(sum(1 for k in state if state[k]))
