import json
import numpy as np
from typing import List, Tuple


with open('data.json', 'r') as f:
    data = np.array(json.load(f))


def get_next_point(map_of_points: np.ndarray,
                   current: np.ndarray) -> np.ndarray:
    for y, horz in enumerate(map_of_points):
        # print(f"***{y}**")
        for x, point in enumerate(horz):
            # print(f"+++{x}+++")
            if point == 1 and y >= current[1] and (x > current[0] or y > current[1]):
                return np.array((x, y))
    raise ValueError("No points left")


def direction(base, p1) -> int:
    if base[0] > p1[0] or (base[0] >= p1[0] and base[1] > p1[1]):
        return 1
    elif base[0] < p1[0] or (base[0] <= p1[0] and base[1] < p1[1]):
        return -1


def get_all_line_slopes(point: np.ndarray, map_of_points: np.ndarray) -> List[Tuple[float, int]]:
    finals = []

    for y, horz in enumerate(map_of_points):
        for x, ele in enumerate(horz):
            if ele == 1:
                zero = x - point[0]

                finals.append(((y - point[1]) / zero if (zero != 0) else 99999, direction(point, (x, y))))
    return finals


def num_individual_slopes(all_slopes) -> int:
    passed = []
    total = 0
    for slope in all_slopes:
        if slope not in passed:
            passed.append(slope)
            total += 1
    return total


if __name__ == '__main__':
    try:
        counter = 0
        totals = []
        new_point = np.array((-1, -1))
        while True:
            # print(new_point)
            new_point = get_next_point(data, new_point)

            slopes = get_all_line_slopes(new_point, data)
            a = num_individual_slopes(slopes)
            a -= 1
            totals.append(a)
            if counter == 289:
                print(a)
                break
            counter += 1
    except ValueError:
        print(totals[289])
        print(max(totals))

