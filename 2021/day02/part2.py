import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict

with open("data.txt", 'r') as f:
    data = f.readlines()

pos = 0
aim = 0
depth = 0
for d in data:
    cmd, num = d.split()
    num = int(num)
    if cmd == "up":
        aim -= num
    elif cmd == "down":
        aim += num
    elif cmd == "forward":
        pos += num
        depth += aim * num
print(pos*depth)