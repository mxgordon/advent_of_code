import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict

with open("data.txt", 'r') as f:
    data = f.readlines()

pos = 0
depth = 0
for d in data:
    cmd, num = d.split()
    num = int(num)
    if cmd == "up":
        depth -= num
    elif cmd == "down":
        depth += num
    elif cmd == "forward":
        pos += num
print(pos*depth)