from typing import List, Tuple, Iterable

import numpy as np
import math
from functools import partial, reduce
from itertools import groupby
from collections import defaultdict, Counter


with open("data.txt", 'r') as f:
    data = f.readlines()
    # print(data)
    data = [tuple(w.strip().split(" ") for w in d.strip().split(" | ")) for d in data]
    # print((data))

letters = set("abcdefg")
s = 0
for line in data:
    for l in line[1]:
        if len(l) in [2, 3, 4, 7]:
            s += 1
print(s)



