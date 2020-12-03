import numpy as np
import json
from math import fabs


with open('data.json', 'r') as file:
    instructions = json.load(file)

LINE0 = [[v[0], int(v[1:])] for v in instructions[0]]  # instructions[0]
LINE1 = [[v[0], int(v[1:])] for v in instructions[1]]  # instructions[1]

DIRECTIONS = {"U": np.array([0, 1]),
              "D": np.array([0, -1]),
              "R": np.array([1, 0]),
              "L": np.array([-1, 0])}

points0 = []
position0 = np.array([0, 0])


for direction, distance in LINE0:
    assert direction in DIRECTIONS.keys()
    step = DIRECTIONS[direction]
    for i in range(distance):
        position0 -= step
        points0.append(position0.copy())


points1 = []
position1 = np.array([0, 0])


for direction, distance in LINE1:
    assert direction in DIRECTIONS.keys()
    step = DIRECTIONS[direction]
    for i in range(distance):
        position1 -= step
        points1.append(position1.copy())

distances = []
points1 = np.array(points1)

points1 = [(x, y) for x, y in points1]
points0 = [(x, y) for x, y in points0]

print(len(points0))

for num, point0 in enumerate(points0):
    if num % 1000 == 0: print(f"***{num}")

    if point0 in points1:
        index = points1.index(point0)
        x1, y1 = points1[index]
        distances.append([fabs(x1) + fabs(y1), num, index])


assert points0[0] is not points0[1]

print(2+min([i+iii for ii, i, iii in distances]))
