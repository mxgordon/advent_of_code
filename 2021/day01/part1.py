import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict

with open("data.txt", 'r') as f:
    data = f.readlines()

    data = list(map(int, data))
    print(np.array(data))

data2 = np.array([0] + list(np.array(data)[:-1]))

print((data2 - np.array(data) < 0).sum() - 1)
