import numpy as np
import math
from functools import reduce

with open("data.txt", 'r') as f:
    data = [[*line.strip()] for line in f.readlines()]
    data = np.array(data)

last = data.copy()


def valrc(rc, arr):
    if (rc > 0).all():
        try:
            tmp = arr[rc[0]][rc[1]]
            return True
        except:
            return False
    return False


def get_visible(r, c, arr):
    movements = [*np.array([(-1, -1), (0, -1), (-1, 0), (0, 1), (1, 1), (1, 0), (-1, 1), (1, -1)])]
    center = np.array([r, c])
    surround = list(zip(movements, [center] * 8))
    coords = []

    while len(surround) != 0:
        surround = map(lambda mrc: [mrc[0], mrc[1] + mrc[0]], surround)
        surround = list(filter(lambda mrc: valrc(mrc[1], arr), surround))

        for i, mrc in enumerate(surround):
            m, rc = mrc
            if arr[rc[0]][rc[1]] != '.':
                coords.append(surround.pop(i)[1])
    return list(map(tuple, coords))

print(get_visible(4, 3, data))


l = 0
first = True
while (data != last).any() or first:
    first = False
    l += 1
    print(l)
    last = data.copy()
    for row in range(len(last)):
        for col, val in enumerate(last[row]):
            if val == '.':
                continue
            elif val == "L":
                sf = get_visible(row, col, last)
                # print(sf)
                sf = list(filter(lambda rc: last[rc] == '#', sf))
                if len(sf) == 0:
                    data[row, col] = "#"
            else:
                sf = get_visible(row, col, last)
                sf = list(filter(lambda rc: last[rc] == '#', sf))

                if len(sf) >= 5:
                    data[row, col] = "L"

print(data)
print(((data == '#') * 1).sum())
