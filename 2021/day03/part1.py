import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict

with open("data.txt", 'r') as f:
    data = f.readlines()
    data = [[int(a) for a in d.strip()] for d in data]
    data = np.array(data)

things = np.apply_along_axis(lambda x: np.bincount(x).argmax(), axis=0, arr=data)
g = int("".join([str(t) for t in things]), 2)
e = int("".join([str(0 if t == 1 else 1) for t in things]),2)
print(g*e)
