from typing import List, Tuple, Iterable

import numpy as np
import math
from functools import partial, reduce
from itertools import groupby
from collections import defaultdict, Counter

def group(nums: Tuple[set]):
    d = defaultdict(lambda: [])
    d.update({k: lambda: [*v] for k, v in groupby(nums, key=len)}, )
    return d


def is_1(letters):
    return len(letters) == 2


def is_4(letters):
    return len(letters) == 4


def is_7(letters):
    return len(letters) == 3


def is_8(letters):
    return len(letters) == 8


def is_9(letters, gs):
    return letters.union(gs[2][0]) == letters



with open("data.txt", 'r') as f:
    # data = f.readlines()
    data = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    # print(data)
    data = [tuple(tuple(map(set, w.strip().split(" "))) for w in d.strip().split(" | ")) for d in data]
    # print((data))

letters = set("abcdefg")
s = 0
for line in data:
    disp: Tuple[set] = line[1]
    lens = list(map(len, disp))
    counter = Counter()
    groups = group(disp)

    nums = defaultdict(lambda: set())

    for l in disp:
        if is_1(l):
            nums[1] = l
        elif is_4(l):
            nums[4] = l
        elif is_7(l):
            nums[7] = l
        elif is_8(l):
            nums[8] = l
        elif is_9(l, groups):
            nums[9] = l
            print(l)



    # a = [*disp[lens.index(3)].difference(disp[lens.index(2)])][0]
    #
    # for ele in groups[7]:
    #
    #     diff = disp[lens.index(2)].difference(ele)
    #     print(diff, ele, disp[lens.index(2)], groups[7])
    #     if len(diff) == 1:
    #         c = list(diff)
    #         f = disp[lens.index(2)].difference(diff)
    #         break
    #
    # print(c,f)
    #
    #
    # e = letters.difference(disp[lens.index(7)])
    # print(e)
    # print(group(disp))
print(s)



