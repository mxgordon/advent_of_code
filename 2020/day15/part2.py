data = list(map(int, "9,12,1,4,17,0,18".split(',')))

spoken = {}
last = None

for i, v in enumerate(data):
    spoken[v] = i
    last = v

for i in range(i, 30000000 - 1):
    if last not in spoken.keys():
        nxt = 0
    else:
        nxt = i - spoken[last]

    spoken[last] = i

    if i % 1000000 == 0:
        print(i, nxt)

    last = nxt

print(last)
