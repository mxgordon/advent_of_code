import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict, Counter

with open("data.txt", 'r') as f:
    data = f.readlines()
    data = [d.strip().split("-") for d in data]
    all_caves = set([cave for d in data for cave in d])
    options = dict.fromkeys(all_caves)

    for k in options:
        v = []
        for d in data:
            if d[0] == k:
                v.append(d[1])
            elif d[1] == k:
                v.append(d[0])
        options[k] = v
    print(options)


def make_paths(options, path=None):
    if path is None:
        path = ['start']
    paths = []
    for opt in options[path[-1]]:

        if opt == "end":
            return [path + ["end"]]
        elif (opt.lower() == opt) and (opt not in path):
            print(opt)
            paths += make_paths(options.copy(), path + [opt])
        else:
            o = options.copy()
            print(path)
            new_opt = o[path[-1]]
            new_opt.remove(opt)
            o[path[-1]] = new_opt
            paths += make_paths(o, path+[opt])
    return paths


good_paths = []
all_paths = make_paths(options)
for p in all_paths:
    if p[-1] == 'end':
        good_paths.append(p)

print(len(good_paths), all_paths)
