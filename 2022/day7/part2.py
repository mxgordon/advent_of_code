import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from recordclass import recordclass

with open("data.txt", 'r') as f:
    data = f.read().split("\n$ ")

cmds = []

for cmd in data:
    c, *out = cmd.split("\n")
    cmds.append((c, out))

Folder = recordclass("Folder", "name parent children size")
File = recordclass("File", "name parent size")

root = Folder("/", None, [], None)
cwd = root

del cmds[0]

for cmd, out in cmds:
    if cmd == "ls":
        for file in out:
            size, name = file.split(" ")
            if size == "dir":
                cwd.children.append(Folder(name, cwd, [], None))
            else:
                cwd.children.append(File(name, cwd, int(size)))
    elif cmd.split(" ")[1] == "..":
        cwd = cwd.parent
    elif cmd.split(" ")[1] == "/":
        cwd = root
    else:
        cwd = [*filter(lambda x: isinstance(x, Folder) and x.name == cmd.split(" ")[1], cwd.children)][0]


def update_size(folder: Folder):
    size = 0
    for f in folder.children:
        if isinstance(f, Folder):
            size += update_size(f)
        else:
            size += f.size

    folder.size = size
    return size


def get_folders(folder: Folder):
    folders = []

    for f in folder.children:
        if isinstance(f, Folder):
            folders.append(f)
            folders += get_folders(f)

    return folders

space = 70000000
need = 30000000
max_used = space - need

total_size = update_size(root)
min_fold = total_size - max_used
folders = get_folders(root)

sizes = sorted(map(lambda f: f.size, filter(lambda f: f.size >= min_fold, folders)))
print(sizes[0])
