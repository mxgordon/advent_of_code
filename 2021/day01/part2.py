import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict

with open("data.txt", 'r') as f:
    data = f.readlines()
    
    data = list(map(int, data))
    print(np.array(data))
#
# data2 = np.array([0] + list(np.array(data)[:-1]))
#
# print((data2 - np.array(data) < 0).sum() - 1)
c= 0
big = 0
for i in range(len(data)-2):
    if sum(data[i:i+3]) > big:
        c+=1
    big = sum(data[i:i+3])

print(c-1)
