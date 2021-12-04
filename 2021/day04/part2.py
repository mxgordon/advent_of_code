import numpy as np
import math
from functools import partial, reduce
from collections import defaultdict

with open("data.txt", 'r') as f:
    data = f.readlines()
    nums = list(map(int, data.pop(0).strip().split(",")))

    raw_boards = "".join(data).strip().split("\n\n")
    boards = []

    for rb in raw_boards:
        b = [list(map(int, l.strip().replace("  ", " ").split(" "))) for l in rb.strip().split("\n")]
        boards.append(b)

    boards = np.array(boards)
    selected = np.empty(boards.shape, dtype=bool)
    selected.fill(False)

combos = [(0,), (1,), (2,), (3,), (4,), (slice(None), 0), (slice(None), 1), (slice(None), 2), (slice(None), 3),(slice(None), 4)]
special = [slice(0, None, 6), slice(4, None, 4)]
winners = set()
last = winners.copy()
for n in nums:
    selected[np.where(boards == n)] = True

    for c in combos:
        good = np.where(selected[(slice(None),) + c].sum(1) == 5)[0]
        winners.update(good)

        if len(winners) == len(boards):
            assert len(winners.difference(last)) == 1
            looser = list(winners.difference(last))[0]
            print(np.extract(selected[looser] == False, boards[looser]).sum() * n)
            quit()
    else:
        for s in special:
            good = np.where(selected[:, s].sum(1) == 5)[0]
            winners.update(good)

            if len(winners) == len(boards):
                assert len(winners.difference(last)) == 1

                looser = list(winners.difference(last))[0]
                print(np.extract(selected[looser] == False, boards[looser]).sum() * n)
                quit()
    last = winners.copy()
