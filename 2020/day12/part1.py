import numpy as np
from math import radians, cos, sin


with open("data.txt", 'r') as f:
    data = [(line[0], int(line[1:])) for line in f.readlines()]

loc = np.array([0., 0.])
rot = 0

directions = {
    "N": np.array([0, 1]),
    "S": np.array([0, -1]),
    "E": np.array([1, 0]),
    "W": np.array([-1, 0]),
}


def ftoxy(r, d):
    return np.array([cos(radians(r)) * d, sin(radians(r)) * d])


for direction, distance in data:
    if direction in ["L",  "R"]:
        rot += distance if direction == "L" else (-distance)
    elif direction == "F":
        loc += ftoxy(rot, distance)
    else:
        loc += directions[direction] * distance

print(round(np.abs(loc).sum()))
