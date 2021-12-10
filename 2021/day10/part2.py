import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict, Counter

with open("data.txt", 'r') as f:
    data = f.readlines()
    data = list(map(list, map(str.strip, data)))

brackets = {"{": "}", "[": "]", "(": ")", "<": ">"}
points = []
pt_table = {")": 1, "]": 2, "}": 3, ">": 4}

for line in data:
    opens = line[:1]

    for e in line[1:]:
        if e in brackets.keys():
            opens.append(e)
        else:
            if e == brackets[opens[-1]]:
                del opens[-1]
            else:
                break
    else:
        if len(opens) != 0:
            closers = list(map(pt_table.__getitem__, map(brackets.__getitem__, opens[::-1])))
            points.append(reduce(lambda i, n: (i*5)+n, closers, 0))
points.sort()
print(points[len(points)//2])

