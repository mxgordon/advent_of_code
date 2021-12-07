import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict

with open("data.txt", 'r') as f:
    data = f.read()
    data = list(map(int, data.split(',')))

crabs = np.array(data)
mini = min(crabs)
maxi = max(crabs)

diff = abs(maxi - mini)

crabs = np.array([crabs for _ in range(diff+1)])

pos = np.array([[p]*len(data) for p in range(mini, maxi+1)])

diffs = abs(crabs - pos)
diffs = diffs * (diffs + 1)/2

print(diffs.sum(1).min())
