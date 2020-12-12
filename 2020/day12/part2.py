import numpy as np
from math import radians, cos, sin


with open("data.txt", 'r') as f:
    data = [(line[0], int(line[1:])) for line in f.readlines()]

wp = np.array([10, 1])
loc = np.array([0., 0.])

directions = {
    "N": np.array([0, 1]),
    "S": np.array([0, -1]),
    "E": np.array([1, 0]),
    "W": np.array([-1, 0]),
}


def wprot(direc, d, wploc):
    d2 = d * (1 if direc == "L" else -1)
    return np.array(
        [(cos(radians(d2)) * wploc[0]) - (sin(radians(d2)) * wploc[1]),
         (cos(radians(d2)) * wploc[1]) + (sin(radians(d2)) * wploc[0])])


for direction, distance in data:
    if direction in ["L", "R"]:
        wp = wprot(direction, distance, wp)
    elif direction == "F":
        loc += wp * distance
    else:
        wp += directions[direction] * distance


print(round(np.abs(loc).sum()))
