import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict, Counter

with open("data.txt", 'r') as f:
    data = f.readlines()
