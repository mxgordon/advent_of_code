import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict, Counter

with open("data.txt", 'r') as f:
    data = f.readlines()
    data = list(map(list, map(str.strip, data)))

brackets = {"{": "}", "[": "]", "(": ")", "<": ">"}
points = 0
pt_table = {")": 3, "]": 57, "}": 1197, ">": 25137}

for line in data:
    opens = line[:1]

    for e in line[1:]:
        if e in brackets.keys():
            opens.append(e)
        else:
            if e == brackets[opens[-1]]:
                del opens[-1]
            else:
                points += pt_table[e]
                break
print(points)

