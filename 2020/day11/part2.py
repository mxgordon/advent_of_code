import numpy as np
import math

with open("data.txt", 'r') as f:
    data = [[*line.strip()] for line in f.readlines()]
    data = np.array(data)

last = data.copy()




def get_visible(r, c, arr):
    movements = [*np.array([(-1, -1), (0, -1), (-1, 0), (0, 1), (1, 1), (1, 0), (-1, 1), (1, -1)])]
    coords = []
    start = np.array([r, c])
    for move in movements:
        loc = start + move
        try:
            arr[loc]
            if (loc < 0).any(): raise RuntimeError
        except: continue
        while arr[tuple(loc)] == '.':
            loc += move
            try:
                arr[loc]
                if (loc < 0).any(): raise RuntimeError
            except:
                loc -= move
                break
        coords.append(loc)
    return map(tuple, coords)


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
                sf = [*filter(lambda v: v == '#', [*map(lambda xy: last[xy], sf)])]
                if len(sf) == 0:
                    data[row, col] = "#"
            else:
                sf = get_visible(row, col, last)
                af = [*filter(lambda v: v == '#', map(lambda xy: last[xy], sf))]

                if len(af) >= 5:
                    data[row, col] = "L"

print(data)
print(((data == '#') * 1).sum())