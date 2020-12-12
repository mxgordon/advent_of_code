import numpy as np
import math


with open("data.txt", 'r') as f:
    data = [[*line.strip()] for line in f.readlines()]
    data = np.array(data)

last = data.copy()

def get_adjecent(x,y):
    return filter(lambda xy: 0<=xy[0]<len(data) and 0<=xy[1]<len(data[0]), [(x-1, y-1), (x, y-1), (x-1, y), (x, y+1), (x+1, y+1), (x+1, y), (x-1, y+1), (x+1, y-1)])

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
                sf = get_adjecent(row, col)
                sf = [*filter(lambda v: v == '#', [*map(lambda xy: last[xy], sf)])]
                # print(sf)
                if len(sf) == 0:
                    data[row, col] = "#"
            else:
                sf = get_adjecent(row, col)
                af = [*filter(lambda v: v == '#', map(lambda xy: last[xy], sf))]

                if len(af) >= 5:
                    data[row, col] = "L"

print(data)
print(((data == '#') * 1).sum())